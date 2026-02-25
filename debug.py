import os
import sys

print("Current directory:", os.getcwd())
print("Python path:", sys.path)

try:
    import django
    print("Django version:", django.get_version())
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brandify_project.settings')
    django.setup()
    
    from django.conf import settings
    print("STATIC_ROOT:", settings.STATIC_ROOT)
    print("STATICFILES_DIRS:", settings.STATICFILES_DIRS)
    print("STATICFILES_STORAGE:", settings.STATICFILES_STORAGE)
except Exception as e:
    print("Error:", e)
