"""Create the untracked development secret key once; keep an existing key.

Development settings read DJANGO_SECRET_KEY first and fall back to this file.
Production never reads it.
"""

import os
import secrets
from pathlib import Path

KEY_FILE = Path(__file__).resolve().parent.parent / ".dev-secret-key"

if KEY_FILE.exists():
    print(f"Keeping {KEY_FILE.name}.")
else:
    descriptor = os.open(KEY_FILE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w") as handle:
        handle.write(secrets.token_urlsafe(50) + "\n")
    print(f"Created {KEY_FILE.name}.")
