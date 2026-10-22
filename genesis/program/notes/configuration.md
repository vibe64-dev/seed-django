# Project configuration

Select development or production behavior, the database file and the
browser-facing origin.

## Sources

- Main: `config/settings/base.py`
- `config/settings/development.py`
- `config/settings/production.py`
- `config/urls.py`
- `config/wsgi.py`
- `config/asgi.py`
- `manage.py`
- `gunicorn.conf.py`
- `scripts/create_dev_secret_key.py`
- `requirements.txt`

## Public contract

`manage.py` uses development settings: debug pages, any host unless
`DJANGO_ALLOWED_HOSTS` lists them, framing allowed, and a secret key from
`DJANGO_SECRET_KEY` or the untracked `.dev-secret-key` that
`scripts/create_dev_secret_key.py` creates once. WSGI/ASGI and Gunicorn use
production settings, which require `DJANGO_SECRET_KEY`, allow
`DJANGO_ALLOWED_HOSTS` (default `127.0.0.1,localhost`), send secure cookies and
serve collected static files through WhiteNoise.

Both trust `X-Forwarded-Host`, `X-Forwarded-Port` and `X-Forwarded-Proto` from
the loopback reverse proxy, so redirects and the CSRF origin check use the
browser-facing origin. `DB_NAME` names the SQLite file; without it a standalone
checkout uses `db.sqlite3`. Tests use an in-memory database.
