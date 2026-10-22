"""Production settings: every secret comes from the environment."""

import os

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
if not SECRET_KEY:
    raise ImproperlyConfigured("Set DJANGO_SECRET_KEY for this environment.")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

MAILERS = {
    "default": {
        "BACKEND": os.environ.get(
            "DJANGO_EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
        ),
    },
}
