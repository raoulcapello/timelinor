"""
Staging Settings for Heroku
"""

import django_heroku

# If using in your own project, update the project namespace below
from timelinor.settings.base import *


# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception
    # if not found
    'default': env.db(),
}

# Activate Django-Heroku.
django_heroku.settings(locals())
