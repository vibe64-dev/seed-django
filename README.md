# Django Basic starter

A small Django 6.1 application: a home page with one form that saves short
notes to SQLite and lists the newest ones. No visitor accounts; Django's admin
site is available for staff users you create.

This repository's application branches:

- [basic](https://github.com/vibe64-dev/seed-django/tree/basic): notes app with SQLite.

## Run locally

Install Python 3.12 or newer and Git.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/create_dev_secret_key.py
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000. `scripts/create_dev_secret_key.py` writes an
untracked `.dev-secret-key` once; development settings use it unless
`DJANGO_SECRET_KEY` is set. `DB_NAME` chooses the SQLite file (default
`db.sqlite3`). To use the admin site, run
`.venv/bin/python manage.py createsuperuser`.

## Use through Genesis or Vibe64

See [starting the app](docs/colleague-usage/starting-app.md).

Install `genesis-compiler` and `genesis-stack`, run `genesis init` in an empty
Git repository, then choose `official:django/basic` with
`genesis templates apply`. Vibe64 offers the same starter when you add a
project. Genesis preserves the destination's history and authored project
context; ordinary Git commits or Vibe64 Save keep your new source.

The starter owns its dependencies and the setup, output, deployment and
verification commands in `genesis/stack.md`. Genesis describes those
requirements; Vibe64 runs the declared operations. Workspace setup creates the
virtual environment, installs the pinned requirements, creates the development
secret key and applies migrations before the web output starts. A host may
supply the SQLite filename through `DB_NAME`; the starter never invents one in
source.

## Settings

`manage.py` uses `config.settings.development` (debug on, any host, framing
allowed). `config/wsgi.py`, `config/asgi.py` and Gunicorn use
`config.settings.production`, which needs `DJANGO_SECRET_KEY` and the public
host names in `DJANGO_ALLOWED_HOSTS`. Both trust the `X-Forwarded-Host`,
`X-Forwarded-Port` and `X-Forwarded-Proto` headers of the loopback reverse
proxy they run behind, so CSRF checks and redirects use the browser-facing
address. Keep the server bound to loopback.

Production runs collectstatic and migrations with `--settings
config.settings.production`, then `.venv/bin/gunicorn` reads `gunicorn.conf.py`
and binds `HOST`/`PORT`. Generate a production key with
`python3 -c 'import secrets; print(secrets.token_urlsafe(50))'` and supply it
through your deployment's secret facility. `manage.py check --deploy
--settings config.settings.production` leaves HSTS and HTTPS redirection to
your decision because the proxy terminates HTTPS.

## Check changes

```sh
.venv/bin/python manage.py test
```

Unit tests cover the form and view; `notes/tests/test_http.py` drives the real
HTTP server through forwarded proxy headers, including the CSRF-protected form
POST.

## Keep dependencies current

`requirements.txt` pins every package exactly. To upgrade, install the new
versions in the virtual environment, run the tests, then replace the file with
`.venv/bin/python -m pip freeze` and commit it with any new migrations.
