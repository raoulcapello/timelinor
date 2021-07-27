"""
Local Development Settings
"""

# If using in your own project, update the project namespace below
from timelinor.settings.base import *

INSTALLED_APPS.append('django_extensions')

# Don't send actual emails in development, send them to CLI instead
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Other settings
SITE_PROTOCOL = 'http'  # Used in password reset email
