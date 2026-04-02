import os
from pathlib import Path

<<<<<<< HEAD
# Construir rutas dentro del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de seguridad básica
=======

BASE_DIR = Path(__file__).resolve().parent.parent


>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
SECRET_KEY = 'django-insecure-d)@6ggs&&yfrk$4s1=%a*m9b1q27c0kgspei25fc24^=edi$y!'
DEBUG = True
ALLOWED_HOSTS = []

<<<<<<< HEAD
# Aplicaciones instaladas (Aquí están las de tus amigos y la tuya)
=======
>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Tareas',      
    'categorias', 
    'colorfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

<<<<<<< HEAD
# Configuración de Plantillas (Para que Django encuentre tus carpetas HTML)
=======

>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

<<<<<<< HEAD
# Base de datos (Configurada en modo local para que no te de error de PostgreSQL)
=======

>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD
# Validadores de contraseña
=======

>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

<<<<<<< HEAD
# Configuración de idioma y hora
LANGUAGE_CODE = 'es-co' # Cambiado a español
=======

LANGUAGE_CODE = 'es-co'
>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# Archivos estáticos (CSS, Imágenes)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> fce4a0eefaf7e7ebf328023039da22e74d3a0833
