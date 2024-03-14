from django.db import models

from users.models import NULLABLE


class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, unique=True, **NULLABLE, verbose_name='Телефон')
    education = models.CharField(max_length=300, verbose_name='Образование')
    photo = models.ImageField(upload_to='person/', verbose_name='Фото')

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
