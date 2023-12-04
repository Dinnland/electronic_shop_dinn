from django.contrib.auth.models import AbstractUser
from django.db import models
from . import managers

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Пользователь сервиса"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    # avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.UserManager()
