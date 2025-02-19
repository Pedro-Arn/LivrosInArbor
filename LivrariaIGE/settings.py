import os
# Importação de uma classe de manipulação de caminhos de arquivos e diretórios
from pathlib import Path


# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações iniciais de desenvolvimento 
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Mantenha a chave secreta usada em produção em segredo
SECRET_KEY = "django-insecure-ss7b6bcv+)!%a=%7)&_j*lw)zllqnw*7l--cy2h5s8ljebpw3l"

# Não execute com o modo de debug ativado em produção
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Definição das aplicações
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_select2',
]

CUSTOM_APPS = [
    "apps.autor",
    "apps.curso",
    "apps.livros",
    "apps.usuario",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LivrariaIGE.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LivrariaIGE.wsgi.application"


# Banco de dados
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'LivrariaIGE',
        'USER'    : 'admin',
        'PASSWORD': 'admin',
        'HOST'    : 'localhost',
        'PORT'    : '3306',
    }
}


# Validação de senha
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Tipo de campo chave primária padrão
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_FILE_STORAGE = 'Django.core.files.storage.FileSystemStorage'
