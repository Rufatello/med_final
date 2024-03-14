from django.db import models

from users.models import NULLABLE, User


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


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Фото')
    descriptions = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, verbose_name='Цена', decimal_places=2)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количетсво')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'{self.user.email}, {self.product.name}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'