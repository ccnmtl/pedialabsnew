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
    'registration',
    'pagetree',
    'pageblocks',
    'quizblock',
    'pedialabsnew.main',
    'pedialabsnew.exercises',
    'pedialabsnew.rstplot',
]

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
