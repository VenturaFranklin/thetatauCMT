# Generated by Django 2.2.3 on 2019-08-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_riskmanagement_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskmanagement',
            name='role',
            field=models.CharField(default='officer', max_length=50),
            preserve_default=False,
        ),
    ]