from .base import *
import sys

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]["OPTIONS"].update({"debug": True})

# Less strict password authentication and validation
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = []

# Django Debug Toolbar
# Uncomment to enablae debug mode line below
# INSTALLED_APPS += ("debug_toolbar",)

# Additional middleware introduced by debug toolbar
# Uncomment to enablae debug mode line below
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Show emails to console in DEBUG mode
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Allow internal IPs for debugging
INTERNAL_IPS = ["127.0.0.1", "0.0.0.1"]