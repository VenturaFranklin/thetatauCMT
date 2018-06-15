# Generated by Django 2.0.3 on 2018-06-15 21:49

from django.db import migrations, models


def migrate_data_forward(apps, schema_editor):
    region = apps.get_model("regions", "Region")
    for instance in region.objects.all():
        print(f"Generating slug for {instance}")
        instance.save()  # Will trigger slug update


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_initial_regions_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.SlugField(default=None, null=True, unique=True),
        ),
        migrations.RunPython(migrate_data_forward)
    ]
