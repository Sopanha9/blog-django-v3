"""
Django settings for main project.
"""

from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add apps directory to Python path
sys.path.insert(0, str(BASE_DIR / 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-275$ol_&fs-fylqh(b)w0n!dja3p$l9mc@(o97r*g90eopk85u')

# SECURITY WARNING: don't run with debug turned on in production!
# Set this to False in your Render Environment Variables
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com", # This allows your Render URL to work
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'apps.blog',
    'apps.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # REQUIRED FOR PRODUCTION STATIC FILES
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main' / 'templates', BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database - Note: SQLite data will reset on every deploy on Render!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "resources",
    BASE_DIR / "main" / "static",
]

# FIX: This is what was causing your build error
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use WhiteNoise to handle compression and caching
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CKEditor Configuration
CKEDITOR_UPLOAD_PATH = 'uploads/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 700,
        'width': '100%',
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'extraPlugins': ','.join(['uploadimage', 'image2']),
    },
}

CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_IMAGE_BACKEND = 'pillow'

# Jazzmin Settings
JAZZMIN_SETTINGS = {
    "site_title": "Blog CMS Admin",
    "site_header": "Blog CMS",
    "site_brand": "Blog Management",
    "welcome_sign": "Welcome to Blog CMS Admin Panel",
    "search_model": ["api.Post", "api.Comment"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Site", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "api.Post": "fas fa-blog",
        "api.Comment": "fas fa-comments",
    },
    "changeform_format": "horizontal_tabs",
    "custom_css": "admin/css/custom_admin.css",
}

JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-white navbar-light",
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "theme": "flatly",
}
