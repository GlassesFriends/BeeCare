# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from pathlib import Path
import os

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|
from decouple import config

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|
# |=====|    MODULO DE CLOUDINARY     |=====|
# |=========================================|
import cloudinary
import cloudinary.uploader
import cloudinary.api


# |=============================================================|
# |===============|       DIRECTORIO BASE       |===============|
# |=============================================================|
BASE_DIR = Path(__file__).resolve().parent.parent

# |=============================================================|
# |===============|          SECRET KEY         |===============|
# |=============================================================|
SECRET_KEY = config('SECRET_KEY')

# |=============================================================|
# |===============|       ¿EN DESARROLLO?       |===============|
# |=============================================================|
DEBUG = config('DEBUG', cast=bool)

# |=============================================================|
# |===============|        HOST PERMITIDOS      |===============|
# |=============================================================|
# |=| Los host se añadirán dependiendo de la configuración de |=|
# |=| red de donde se esté desplegando el proyecto.           |=|
# |=============================================================|
ALLOWED_HOSTS = [
    'localhost',        # IP local
    '127.0.0.1',        # IP local
    '192.168.17.75',    # IP de desarrollo 
    '192.168.32.99',    # IP de desarrollo
    '192.168.100.120',  # IP de desarrollo
    'beecare.glassesfriends.com',  # PRODUCCIÓN
    'beecaretest.herokuapp.com',  # Heroku
    'gf-beecare.herokuapp.com',  # Heroku
    ]

# |=============================================================|
# |===============|  APLICACIONES DEL PROYECTO  |===============|
# |=============================================================|
# |=| Se debe dividir a las aplicaciones segun el impacto que |=|
# |=| tendrán en el proyecto.                                 |=|
# |=============================================================|

# |=========================================|
# |=====|       APLICACIONES BASE     |=====|
# |=========================================|
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# |=========================================|
# |=====|     APLICACIONES LOCALES    |=====|
# |=========================================|
LOCAL_APPS = [
    'apps.member',
    # 'apps.post',
    # 'apps.reaction',
    'apps.sighting',
]
# |=========================================|
# |=====|   APLICACIONES DE TERCEROS  |=====|
# |=========================================|
THIRD_APPS = [
    # |=| App del campo color.            |=|
    'colorfield',
    'cloudinary_storage',
    'cloudinary',
]
# |=========================================|
# |=====|   CONJUNTO TOTAL DE APPS    |=====|
# |=========================================|
INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beecare.urls'

# |=============================================================|
# |===============|   TEMPLATES DEL PROYECTO    |===============|
# |=============================================================|
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # |=========================================|
        # |=====| DIRECTORIO BASE DE TEMPLATE |=====|
        # |=========================================|
        'DIRS': [
            (os.path.join(BASE_DIR, 'templates')),
            ],
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

WSGI_APPLICATION = 'beecare.wsgi.application'

# |=============================================================|
# |===============| BASES DE DATOS DEL PROYECTO |===============|
# |=============================================================|
# |=| Solo se debe mantener una base de datos activa.         |=|
# |=============================================================|

# |=========================================|
# |=====| BASE DE DATOS DE DESARROLLO |=====|
# |=========================================|
# |=| Es la base de datos que se utiliza  |=|
# |=| para el desarrollo del proyecto,    |=|
# |=| jamás se deberá utilizar en         |=|
# |=| producción.                         |=|
# |=========================================|
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / config('SQL_DB_D'),
#     }
# }
 
# |=========================================|
# |=====| BASE DE DATOS DE PRODUCCIÓN |=====|
# |=========================================|
# |=| Se trata de la instancia dentro del |=|
# |=| servidor del proyecto.              |=|
# |=|                                     |=|
# |=| La configuración de este dependerá  |=|
# |=| de las instrucciones del cliente.   |=|
# |=|                                     |=|
# |=| Para el caso del desarrollo de este |=|
# |=| proyecto, se manejarán tres tipos   |=|
# |=| de bases de datos, de [D]esarrollo, |=|
# |=| de pruebas[T] y de [P]roducción.    |=|
# |=========================================|
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': config('SQL_DB_T'),
        'USER': config('SQL_USER'),
        'PASSWORD': config('SQL_PASSWORD'),
        'HOST': 'beecare.database.windows.net' + config('SQL_INSTANCE'),
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server', },
    }
}

# |=============================================================|
# |===============|  Validación de contraseñas  |===============|
# |=============================================================|

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# |=============================================================|
# |===============|    CONFIGURACIÓN GENERAL    |===============|
# |=============================================================|

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# |=============================================================|
# |===============|      ARCHIVOS ESTÁTICOS     |===============|
# |=============================================================|
# |=|  La ruta de archivos estaticos permitirá agregar los    |=|
# |=|  estilos y archivos de javascript a nuestra app web.    |=|
# |=============================================================|

STATIC_ROOT='/static/'
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# |=========================================|
# |=====|  DIRECTORIO DE MULTIMEDIA   |=====|
# |=========================================|
# |=| Esta ruta se utilizará para los     |=|
# |=| archivos multimedia del proyecto.   |=|
# |=========================================|

# |=========================================|
# |=====|  DIRECTORIO DE MULTIMEDIA   |=====|
# |=========================================|
# |=====|     MEDIA DE CLOUDINARY     |=====|
# |=========================================|

MEDIA_URL = '/Beecare/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# |=========================================|
# |====| PERMISOS CLOUDINARY CONEXIÓN  |====|
# |=========================================|

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY':  config('API_KEY'),
    'API_SECRET':  config('API_SECRET'),
}

