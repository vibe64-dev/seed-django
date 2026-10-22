# App Agent Instructions

Use current project context and the official Django documentation for the
pinned version as the source of truth: `https://docs.djangoproject.com/en/6.1/`.

Prefer Django's own apps, models, forms, views, templates, messages, admin and
management commands. After model changes run
`.venv/bin/python manage.py makemigrations` and commit the migration. Add new
packages to `requirements.txt` with an exact version.

Keep secrets out of source: development uses `.dev-secret-key` or
`DJANGO_SECRET_KEY`; production requires `DJANGO_SECRET_KEY`. Keep the server
bound to the supplied loopback host and port.

Pages start with useful content and actions. Do not add a page header, welcome
heading, or standalone title unless the user asks for one. Keep changes scoped
to the user request and run `.venv/bin/python manage.py test`.
