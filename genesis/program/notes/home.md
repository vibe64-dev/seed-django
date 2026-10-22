# Notes home

Visitors write short notes and see the most recent ones.

## Sources

- Main: `notes/views.py`
- `notes/models.py`
- `notes/forms.py`
- `notes/admin.py`
- `notes/templates/notes/base.html`
- `notes/templates/notes/home.html`
- `notes/static/notes/site.css`
- `notes/migrations/0001_initial.py`
- `notes/tests/test_notes.py`
- `notes/tests/test_http.py`

## Public contract

`GET /` shows the note form and up to twenty most recent notes, newest first,
or "No notes yet." when there are none.

`POST /` with a CSRF token and `text` saves a note of 1 to 280 characters after
trimming surrounding whitespace, then redirects to `/` and confirms "Note
saved." Blank or over-long text re-renders the form with an error and saves
nothing. A POST without a valid CSRF token is rejected with 403.

Staff manage notes in the administration site at `/admin/`.
