"""
WSGI config for dictionary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

port = os.environ.get("PORT")
if port:
    os.environ["DJANGO_PORT"] = port

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dictionary.settings")

application = get_wsgi_application()
