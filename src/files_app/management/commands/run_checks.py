from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models.functions import Coalesce

from files_app.models import File
from files_app.tasks import process_file


class Command(BaseCommand):
    help = "Run check on created files"

    def handle(self, *args, **kwargs):
        files = (
            apps.get_model("files_app.File")
            .objects.filter(status=File.FileStatus.CREATED)
            .order_by(Coalesce("modified", "created").asc())
        )
        for file in files:
            self.stdout.write(self.style.SUCCESS(f"Created file:{file.name}"))
            process_file.delay(file.pk)
        self.stdout.write(self.style.SUCCESS("Done."))
