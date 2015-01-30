from .base import *

INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

STAGE = 'development'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s module=%(module)s, '
            'process_id=%(process)d, %(message)s'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'celery': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

