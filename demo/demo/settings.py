# """
# Django settings for demo project.
#
# Generated by 'django-admin startproject' using Django 5.1.2.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """
#
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-2z&-on!1%-=^r&ow^m62l(!543yn(h$k@6wictn258suf4gy-5'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'myapp'
#     # 'rest_framework'
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'demo.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# # Use database-backed sessions
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
#
# # Set the session cookie age (optional, defaults to 2 weeks)
# SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
#
# # Ensure the session cookie is sent only over secure connections (optional, for production)
# # SESSION_COOKIE_SECURE = True
#
# # Prevent session hijacking
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep the session alive after closing the browser
#
#
# WSGI_APPLICATION = 'demo.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#
# DATABASES = {
#     'legacy': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'csci467',
#         'USER': 'student',
#         'PASSWORD': 'student',
#         'HOST': 'blitz.cs.niu.edu',
#         'PORT': '3306',
#     },
#
# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'csci_513_database',  # Replace with your new database name
#         'USER': 'csci_513_proj',            # Replace with the username for the new database
#         'PASSWORD': 'Muntazir123@',    # Replace with the password for the new database
#         'HOST': 'localhost',           # Assuming this database is local, change if necessary
#         'PORT': '3306',                # Port for MySQL
#     }
#
# }
#
#
#
# # 'blitz.cs.niu.edu',
# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/
#
# STATIC_URL = 'static/'
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DATABASE_ROUTERS = ['demo.db_routers.LegacyRouter']


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2z&-on!1%-=^r&ow^m62l(!543yn(h$k@6wictn258suf4gy-5'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    # 'rest_framework',
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

ROOT_URLCONF = 'demo.urls'

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

WSGI_APPLICATION = 'demo.wsgi.application'

DATABASES = {
    'legacy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csci467',
        'USER': 'student',
        'PASSWORD': 'student',
        'HOST': 'blitz.cs.niu.edu',
        'PORT': '3306',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csci_513_database',
        'USER': 'csci_513_proj',
        'PASSWORD': 'Muntazir123@',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['demo.db_routers.LegacyRouter']

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings for Gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ibrahimalazhar264@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'yugg qsam qewb wyng'  # Replace with your Gmail password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False



