# Generated by Django 5.0.6 on 2024-06-04 16:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="number_of_employees",
        ),
    ]
