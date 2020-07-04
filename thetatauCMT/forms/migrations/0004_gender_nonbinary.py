# Generated by Django 2.2.12 on 2020-07-04 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0003_auto_20200517_1027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pledge",
            name="title",
            field=models.CharField(
                choices=[
                    ("mr", "Mr."),
                    ("miss", "Miss"),
                    ("ms", "Ms"),
                    ("mrs", "Mrs"),
                    ("mx", "Mx"),
                    ("none", ""),
                ],
                max_length=5,
            ),
        ),
    ]
