# Generated by Django 2.2.3 on 2019-10-07 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0002_auto_20191006_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballotcomplete',
            name='motion',
            field=models.CharField(choices=[('aye', 'Aye'), ('nay', 'Nay'), ('abstain', 'Abstain'), ('incomplete', 'Incomplete')], max_length=20),
        ),
    ]
