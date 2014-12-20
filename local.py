from .common import *

MEDIA_URL = "/media/"
STATIC_URL = "static/"
ADMIN_MEDIA_PREFIX = "/static/admin/"

# This should change if you want generate urls in emails
# for external dns.
SITES["front"]["domain"] = "localhost:8000"

DEBUG = True
TEMPLATE_DEBUG = True

#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = False

# GITHUP SETTINGS
GITHUB_API_CLIENT_ID = None
GITHUB_API_CLIENT_SECRET = None

DEFAULT_FROM_EMAIL = "no-reply@example.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
    "rest_framework.renderers.JSONRenderer",
)
