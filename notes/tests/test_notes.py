from django.test import TestCase
from django.urls import reverse

from notes.forms import NoteForm
from notes.models import Note


class NoteFormTests(TestCase):
    def test_trims_text(self):
        form = NoteForm(data={"text": "  Buy milk  "})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["text"], "Buy milk")

    def test_rejects_blank_text(self):
        form = NoteForm(data={"text": "   "})
        self.assertFalse(form.is_valid())

    def test_rejects_text_over_280_characters(self):
        self.assertFalse(NoteForm(data={"text": "x" * 281}).is_valid())


class HomeViewTests(TestCase):
    def test_lists_newest_note_first(self):
        Note.objects.create(text="first")
        Note.objects.create(text="second")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual([note.text for note in response.context["notes"]], ["second", "first"])

    def test_post_saves_and_redirects(self):
        response = self.client.post(reverse("home"), {"text": "Hello"}, follow=True)
        self.assertRedirects(response, reverse("home"))
        self.assertContains(response, "Note saved.")
        self.assertTrue(Note.objects.filter(text="Hello").exists())

    def test_invalid_post_shows_error_and_saves_nothing(self):
        response = self.client.post(reverse("home"), {"text": ""})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.exists())
