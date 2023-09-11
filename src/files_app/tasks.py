import time

from celery import shared_task
from django.core.mail import send_mail
from django.core.management import call_command

from .models import Files, Logs


@shared_task
def send_report(log_id: Logs.pk):
    log = Logs.objects.get(pk=log_id)
    send_mail(
        f"File {log.file.name} checked",
        log.log,
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    Logs.objects.create(log="Report sent", file=log.file)


@shared_task
def process_file(file_id: Files.pk):
    file = Files.objects.get(pk=file_id)
    file.status = Files.FileStatus.QUEUED
    file.save(update_fields=['status'])
    time.sleep(10)
    file = Files.objects.get(pk=file_id)
    file.status = Files.FileStatus.CHECKED
    file.save(update_fields=['status'])
    log = Logs.objects.create(log="Check completed", file=file)
    send_report.delay(log.pk)


@shared_task
def start_run_checks():
    call_command(
        "run_checks",
    )
