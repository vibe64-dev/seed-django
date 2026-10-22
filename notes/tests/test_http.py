"""Exercise the real HTTP server the way a browser behind a proxy does."""

import re
from http.cookiejar import CookieJar
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from notes.models import Note

PUBLIC_ORIGIN = "https://notes.example.test"
FORWARDED = {
    "X-Forwarded-Host": "notes.example.test",
    "X-Forwarded-Proto": "https",
    "X-Forwarded-Port": "443",
}


class FormOverHttpTests(StaticLiveServerTestCase):
    def setUp(self):
        self.cookies = CookieJar()
        self.browser = build_opener(HTTPCookieProcessor(self.cookies))

    def open(self, method="GET", data=None, headers=None):
        request = Request(self.live_server_url + "/", data=data, method=method, headers={**FORWARDED, **(headers or {})})
        return self.browser.open(request, timeout=10)

    def test_proxied_form_post_passes_csrf_and_persists(self):
        page = self.open().read().decode()
        token = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', page).group(1)

        body = urlencode({"csrfmiddlewaretoken": token, "text": "Saved over HTTP"}).encode()
        response = self.open("POST", body, {"Origin": PUBLIC_ORIGIN, "Referer": PUBLIC_ORIGIN + "/"})

        self.assertEqual(response.status, 200)
        self.assertEqual(response.url, self.live_server_url + "/")
        self.assertIn("Saved over HTTP", response.read().decode())
        self.assertTrue(Note.objects.filter(text="Saved over HTTP").exists())

    def test_post_without_csrf_token_is_rejected(self):
        body = urlencode({"text": "Forged"}).encode()
        with self.assertRaises(HTTPError) as raised:
            self.open("POST", body, {"Origin": PUBLIC_ORIGIN})
        self.assertEqual(raised.exception.code, 403)
        self.assertFalse(Note.objects.exists())

    def test_stylesheet_is_served(self):
        response = self.browser.open(self.live_server_url + "/static/notes/site.css", timeout=10)
        self.assertEqual(response.status, 200)
