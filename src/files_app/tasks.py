import time

from celery import shared_task

from .models import Files


@shared_task
def process_file(file_id: Files.pk):
    time.sleep(10)
    Files.objects.filter(pk=file_id).update(status="CH")
