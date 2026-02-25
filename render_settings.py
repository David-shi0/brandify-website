from brandify_project.settings import *

# Override static files settings for Render
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(__file__), 'static'),
    os.path.join(os.path.dirname(__file__), 'core/static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Make sure these directories exist
os.makedirs(STATIC_ROOT, exist_ok=True)
