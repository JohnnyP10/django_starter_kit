from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

def custom_show_toolbar(self):
    return True

DEBUG_TOOLBAR_PATCH_SETTINGS = True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'django_starter_kit.settings.dev.custom_show_toolbar',
}

INTERNAL_IPS = ('127.0.0.1', '128.91.*.*',)

ROLLBAR = {
    'access_token': 'YOUR_POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development',
    'branch': 'develop',
    'root': '/var/www/html/<app>',
}

# If overriding Django's default logging:
# from .logging import *