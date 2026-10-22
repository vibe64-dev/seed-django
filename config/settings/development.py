"""Development settings: debug pages, a local secret key, framing allowed."""

import os

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403
from .base import BASE_DIR, MIDDLEWARE, env_list

DEBUG = True

# The browser-facing development host is not known in advance.
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", ["*"])

# runserver serves static files while DEBUG is on, and development tools may
# show the app inside a frame. Production keeps WhiteNoise and X-Frame-Options.
MIDDLEWARE = [
    m
    for m in MIDDLEWARE
    if m
    not in {
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    }
]

DEV_SECRET_KEY_FILE = BASE_DIR / ".dev-secret-key"


def development_secret_key():
    value = os.environ.get("DJANGO_SECRET_KEY")
    if value:
        return value
    try:
        return DEV_SECRET_KEY_FILE.read_text().strip()
    except FileNotFoundError:
        raise ImproperlyConfigured(
            "Set DJANGO_SECRET_KEY or run "
            "`.venv/bin/python scripts/create_dev_secret_key.py` once."
        ) from None


SECRET_KEY = development_secret_key()
