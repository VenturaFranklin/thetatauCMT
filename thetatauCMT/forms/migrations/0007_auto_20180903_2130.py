# Generated by Django 2.0.3 on 2018-09-04 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20180903_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depledge',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='initiation',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='statuschange',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]