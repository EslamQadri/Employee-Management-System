# Generated by Django 5.0.6 on 2024-06-04 14:13

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
        ("department", "0001_initial"),
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccounts",
            name="is_emp",
            field=models.BooleanField(default=True, verbose_name="Employee"),
        ),
        migrations.AlterField(
            model_name="useraccounts",
            name="is_manager",
            field=models.BooleanField(default=False, verbose_name="Manager"),
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employee_status",
                    models.CharField(
                        choices=[
                            ("ApplicationReceived", "Application Received"),
                            ("InterviewScheduled", "Interview Scheduled"),
                            ("Hired", "Hired"),
                            ("NotAccepted", "Not Accepted"),
                        ],
                        max_length=50,
                        verbose_name="Employee Status",
                    ),
                ),
                (
                    "employee_name",
                    models.CharField(max_length=500, verbose_name="Employee Name"),
                ),
                (
                    "email_address",
                    models.EmailField(max_length=254, verbose_name="Email Address"),
                ),
                (
                    "mobile_number",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Mobile number must be entered in the format: '01xxxxxxxxx'",
                                regex="^01\\d{9}$",
                            )
                        ],
                        verbose_name="Mobile Number",
                    ),
                ),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "designation",
                    models.CharField(
                        help_text="Position or Title",
                        max_length=144,
                        verbose_name="Designation ",
                    ),
                ),
                ("hired_on", models.DateField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="company.company",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.department",
                    ),
                ),
                (
                    "employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]