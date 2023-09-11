from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models.functions import Coalesce

from files_app.tasks import process_file
from files_app.models import Files


class Command(BaseCommand):
    help = "Run check on created files"

    def handle(self, *args, **kwargs):
        files = (
            apps.get_model("files_app.Files")
            .objects.filter(status=Files.FileStatus.CREATED)
            .order_by(Coalesce("modified", "created").asc())
        )
        for f in files:
            self.stdout.write(self.style.SUCCESS(f"Created file:{f.name}"))
            process_file.delay(f.pk)
        self.stdout.write(self.style.SUCCESS("Done."))
