# Generated by Django 4.2.1 on 2023-06-13 20:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("epicevents", "0001_initial"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Event_status",
            new_name="EventStatus",
        ),
    ]
