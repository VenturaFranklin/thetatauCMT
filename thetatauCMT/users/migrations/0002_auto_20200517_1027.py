# Generated by Django 2.2.12 on 2020-05-17 17:27

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="address",
            field=address.models.AddressField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="address.Address",
            ),
        ),
    ]
