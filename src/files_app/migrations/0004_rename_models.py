# Generated by Django 4.2.4 on 2023-09-14 19:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("files_app", "0003_added_logs"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CR", "Created"),
                            ("QU", "Queued"),
                            ("CH", "Checked"),
                        ],
                        default="CR",
                        max_length=2,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/",
                        validators=[
                            django.core.validators.FileExtensionValidator(["py"])
                        ],
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameModel(
            old_name="Logs",
            new_name="Log",
        ),
        migrations.RenameField(
            model_name="log",
            old_name="log",
            new_name="log_txt",
        ),
        migrations.DeleteModel(
            name="Files",
        ),
        migrations.AlterField(
            model_name="log",
            name="file",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="files_app.file",
                verbose_name="File",
            ),
        ),
    ]
