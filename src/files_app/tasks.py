import time

from celery import shared_task
from django.core.management import call_command

from .models import Files


@shared_task
def process_file(file_id: Files.pk):
    time.sleep(10)
    Files.objects.filter(pk=file_id).update(status="CH")


@shared_task
def start_run_checks():
    call_command(
        "run_checks",
    )
