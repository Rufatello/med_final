import pytz
import logging
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django_apscheduler.jobstores import DjangoJobStore
from person.models import Appointment

logger = logging.getLogger(__name__)


def my_job():
    """переодическая задача по отправке письма с записью к врачу"""
    timezone.activate('Europe/Moscow')
    today = datetime.now()
    moscow_tz = pytz.timezone('Europe/Moscow')
    today = today.astimezone(moscow_tz)
    appointments = Appointment.objects.all()

    for appointment in appointments:
        appointment_datetime = datetime.combine(appointment.data, appointment.time).replace(tzinfo=moscow_tz)
        if today >= appointment_datetime:
            user = appointment.user
            send_mail(
                subject='Запись к врачу',
                message=f'Вы записаны к врачу на {appointment.data} в {appointment.time}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()