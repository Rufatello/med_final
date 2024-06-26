from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Комманда создая суперюзера"""
    def handle(self, *args, **options):
        user = User.objects.create(
            is_staff=True,
            is_active=True,
            is_superuser=True,
            first_name='Rufat',
            last_name='Geydarov',
            email='1@mail.ru'
        )
        user.set_password('12345')
        user.save()