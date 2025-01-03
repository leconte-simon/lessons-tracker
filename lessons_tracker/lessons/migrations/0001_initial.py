# Generated by Django 5.1.2 on 2024-11-11 21:51

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassLevel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ClassSubject",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "parent_phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("address", models.TextField(null=True)),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lessons.classlevel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "duration",
                    models.DurationField(default=datetime.timedelta(seconds=3600)),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.0)]
                    ),
                ),
                ("paid", models.BooleanField()),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lessons.classsubject",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lessons.student",
                    ),
                ),
            ],
        ),
    ]
