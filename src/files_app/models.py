from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from django_project.models import TimestampedModel


class Files(TimestampedModel):
    class FileStatus(models.TextChoices):
        CREATED = "CR", "Created"
        UPLOADED = "UP", "Uploaded"
        CHECKED = "CH", "Checked"

    status = models.CharField(
        max_length=2,
        choices=FileStatus.choices,
        default=FileStatus.CREATED,
    )
    name = models.CharField(max_length=50)

    file = models.FileField(
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["py"])],
        upload_to="uploads/",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("files_detail", kwargs={"pk": self.pk})
