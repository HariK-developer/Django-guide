"""
WSGI config for django_guide project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django_guide.settings.base import DEBUG 
from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_guide.settings.development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_guide.settings.production")


application = get_wsgi_application()

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"