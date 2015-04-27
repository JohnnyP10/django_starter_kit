## Error & Log Exception Settings ##

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DEBUG = True

# Rollbar settings. Rollbar handles app exceptions only.
# For more information on how to integrate rollbar, go here https://github.com/rollbar/pyrollbar

ROLLBAR = {
    'access_token': 'YOUR_POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'develop',
    'root': '/path/to/code/root',
}

# If you want to override Django's default logging, you
# can do that by creating a logging dictionary configuration like the
# example below and importing it in your base settings. You can
# then create logging calls in your code. 
# To learn more about Django Logging go here https://docs.djangoproject.com/en/1.7/topics/logging.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
	    'verbose': {
		     'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
         'datefmt' : "%d/%b/%Y %H:%M:%S"
	    },
	    'simple': {
		    'format': '%(levelname)s %(message)s',
	    },
	    
    },
    'filters': {
	    'require_debug_false' : {
		    '()': 'django.utils.log.RequireDebugFalse',
	    },
	    'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
      },
    },
    'handlers': {
        #'file': {  ## uncomment to add log file. You have to create the directory and file as well. ##
            #'level': 'DEBUG',
            #'class': 'logging.FileHandler',
            #'filters': ['require_debug_true'],
            #'filename': BASE_DIR + '/logs/log_file.log', 
        #},
        'console': {
	        'level': 'DEBUG',
	        'class': 'logging.StreamHandler',
	        'formatter': 'simple'
        },
	      'mail_admins': {
		      'level': 'CRITICAL',
		      'filters' : ['require_debug_false'],
		      'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
	      },
    },
    'loggers': {
	      #'django.request': {
           # 'handlers': ['file'],
           # 'level': 'DEBUG',
           # 'propagate': True,
        #},
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
	        'handlers': ['mail_admins'],
	        'level': 'CRITICAL',
	        'propagate': False,
        },
    },
}