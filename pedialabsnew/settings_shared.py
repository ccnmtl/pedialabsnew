# Django settings for pedialabsnew project.
import os.path
from ccnmtlsettings.shared import common

project = 'pedialabsnew'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'pedialabsnew.main',
    'pedialabsnew.exercises',
]

USE_TZ = True

TEMPLATES[0]['OPTIONS']['context_processors'].append(  # noqa
    'pedialabsnew.main.views.context_processor'
)

INSTALLED_APPS += [  # noqa
    'bootstrap3',
    'sorl.thumbnail',
    'bootstrapform',
    'django_extensions',
    'django_cas_ng',
    'registration',
    'pagetree',
    'pageblocks',
    'quizblock',
    'pedialabsnew.main',
    'pedialabsnew.exercises',
    'pedialabsnew.rstplot',
]

INSTALLED_APPS.remove('djangowind') # noqa

PAGEBLOCKS = [
    'pageblocks.TextBlock',
    'pageblocks.HTMLBlock',
    'pageblocks.PullQuoteBlock',
    'pageblocks.ImageBlock',
    'pageblocks.ImagePullQuoteBlock',
    'quizblock.Quiz',
    'exercises.Lab',
    'rstplot.RstPlotBlock',
]

ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE += [  # noqa
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cas_ng.middleware.CASMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend'
]

CAS_SERVER_URL = 'https://cas.columbia.edu/cas/'
CAS_VERSION = '3'
CAS_ADMIN_REDIRECT = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(base, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'stagingcontext.staging_processor',
                'gacontext.ga_processor',
            ],
        },
    },
]
