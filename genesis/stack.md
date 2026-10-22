# Stack

## Stack packages
- `genesis-stack`

## Components
- `python`
- `django`
- `sqlite`
- `django-sqlite`

## Resources

```json genesis-resource
{
  "id": "database",
  "kind": "sqlite",
  "environmentAlternatives": [
    {
      "bindings": {
        "database": "DB_NAME"
      },
      "preferred": true
    }
  ]
}
```

## Verification

- Verify `application`: `.venv/bin/python` `manage.py` `test` `--noinput` `--keepdb`

## Connected development

- Default package type: `pip`

## Deployment

- Runtimes: `python`
- Recreate on restore: `.venv`
- Ready when: `GET` `/admin/login/` returns `200`
- Prepare `Create virtual environment`: `python3` `-m` `venv` `.venv`
- Prepare `Install dependencies`: `.venv/bin/python` `-m` `pip` `install` `-r` `requirements.txt`
- Build `Collect static files`: `.venv/bin/python` `manage.py` `collectstatic` `--noinput` `--settings` `config.settings.production`
- Migrate `Apply migrations`: `.venv/bin/python` `manage.py` `migrate` `--noinput` `--settings` `config.settings.production`
- Serve `Start`: `.venv/bin/gunicorn`

## Outputs

### Target `app`: Run Django app

- Default.
- Mode: `interactive`
- Runtimes: `python`
- Run `Develop`: `.venv/bin/python` `manage.py` `runserver` `{host}:{port}`

#### Presentation

- Kind: `web`
- Preferred port: `8000`
- URL path: `/`
- Ready when: `GET` `/admin/login/` returns `200`

## Workspace setup

- Prepare `Create virtual environment` with `python` when `manage.py` exists: `python3` `-m` `venv` `.venv`
- Prepare `Install Python dependencies` with `python` if `requirements.txt` exists: `.venv/bin/python` `-m` `pip` `install` `-r` `requirements.txt`
- Prepare `Create development secret key` with `python` when `manage.py` exists: `.venv/bin/python` `scripts/create_dev_secret_key.py`
- Prepare `Apply migrations` with `python` when `manage.py` exists: `.venv/bin/python` `manage.py` `migrate` `--noinput`
