# Generated by Django 3.1.3 on 2021-01-13 20:21

import ctfhub.helpers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ctfhub", "0003_auto_20210113_1945"),
    ]

    operations = [
        migrations.AddField(
            model_name="ctf",
            name="note_id",
            field=models.CharField(
                blank=True, default=ctfhub.helpers.create_new_note, max_length=38
            ),
        ),
    ]