import time

from celery import shared_task
from django.core.mail import send_mail
from django.core.management import call_command

from .models import File, Log


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def send_report(self, log_id: Log.pk):
    log = Log.objects.get(pk=log_id)
    send_mail(
        f"File {log.file.name} checked",
        log.log_txt,
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    Log.objects.create(log_txt="Report sent", file=log.file)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 7, "countdown": 5},
)
def process_file(self, file_id: File.pk):
    file = File.objects.get(pk=file_id)
    file.status = File.FileStatus.QUEUED
    file.save(update_fields=["status"])
    time.sleep(10)
    file = File.objects.get(pk=file_id)
    file.status = File.FileStatus.CHECKED
    file.save(update_fields=["status"])
    log = Log.objects.create(log_txt="Check completed", file=file)
    send_report.delay(log.pk)


@shared_task
def start_run_checks():
    call_command(
        "run_checks",
    )
