# Generated by Django 2.2.12 on 2020-07-20 02:31

from django.db import migrations, models
import forms.models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0009_auto_20200719_1925"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disciplinaryprocess",
            name="minutes",
            field=models.FileField(
                blank=True,
                help_text="Please attach a copy of the minutes from the meeting where the trial was held.",
                null=True,
                upload_to=forms.models.get_discipline_upload_path,
            ),
        ),
    ]
