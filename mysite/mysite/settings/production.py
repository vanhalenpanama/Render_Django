# myproject/settings/production.py
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['render-django-amp9.onrender.com', '13.228.225.19']