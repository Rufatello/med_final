import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse


def generation():
    '''Генерация кода для подтверждения регистрации'''
    password = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return password


def new_pass(request):
    """Генерация пароля и отправка его на почту"""
    new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    send_mail(
        subject='Новый пароль',
        message=f'Новый пароль {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('user:login'))