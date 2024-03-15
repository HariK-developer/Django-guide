"""
ASGI config for django_guide project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django_guide.settings.base import DEBUG


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_guide.settings.development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_guide.settings.production")

application = get_asgi_application()
