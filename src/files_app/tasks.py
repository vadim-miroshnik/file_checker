import time

from celery import shared_task
from django.core.management import call_command

from .models import Files, Logs


@shared_task
def process_file(file_id: Files.pk):
    file = Files.objects.filter(pk=file_id).first()
    file.status = "UP"
    file.save()
    time.sleep(10)
    file = Files.objects.filter(pk=file_id).first()
    file.status = "CH"
    file.save()
    Logs.objects.create(log="check completed", file=file)


@shared_task
def start_run_checks():
    call_command(
        "run_checks",
    )
