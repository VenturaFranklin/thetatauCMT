# Generated by Django 2.0.3 on 2018-12-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20181021_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Member Name'),
        ),
    ]
