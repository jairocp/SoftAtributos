"""
WSGI config for cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name
from dj_static  import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("cms"))

application = Cling(get_wsgi_application())