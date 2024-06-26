from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """комманда для создания json файла с записями из БД"""
    def handle(self, *args, **options):
        call_command('dumpdata', 'person', output='data.json')
        call_command('loaddata', 'data.json')