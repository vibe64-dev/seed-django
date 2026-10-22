import os

wsgi_app = "config.wsgi"
bind = f"{os.environ.get('HOST', '127.0.0.1')}:{os.environ.get('PORT', '8000')}"
# SQLite allows one writer at a time; keep the worker count small.
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
accesslog = "-"
