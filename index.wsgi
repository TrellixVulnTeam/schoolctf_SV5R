"""
WSGI config for scorry project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/var/www/py3env/lib/python3.5/site-packages')

sys.path.append('/var/www')
sys.path.append('/var/www/scorry')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scorry.settings")

activate_env='/var/www/py3env/bin/activate_this.py'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
