# Generated by Django 2.2.12 on 2020-08-31 05:06

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("content", ckeditor.fields.RichTextField()),
                (
                    "priority",
                    models.IntegerField(
                        choices=[
                            (1, 1),
                            (2, 2),
                            (3, 3),
                            (4, 4),
                            (5, 5),
                            (6, 6),
                            (7, 7),
                            (8, 8),
                            (9, 9),
                            (10, 10),
                        ],
                        default=10,
                        help_text="The order you want announcements to appear in, 1 will be on top. Sorted by priority and then reverse published start date",
                        verbose_name="Priority order, 1 highest",
                    ),
                ),
                (
                    "publish_start",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "publish_end",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=255, unique=True, verbose_name="Slug"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
            ],
            options={
                "verbose_name": "Announcement",
                "ordering": ["priority", "-publish_start"],
            },
        ),
    ]
