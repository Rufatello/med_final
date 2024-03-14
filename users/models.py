from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=50, verbose_name='Почта')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    code = models.CharField(max_length=15, verbose_name='код', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', **NULLABLE, verbose_name='Аватар')
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
