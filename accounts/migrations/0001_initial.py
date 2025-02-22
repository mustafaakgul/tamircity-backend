# Generated by Django 4.1.7 on 2023-04-15 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("brands", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("device_types", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TechService",
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
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("twitter", models.CharField(blank=True, max_length=200, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tech_services",
                        to="brands.brand",
                    ),
                ),
                (
                    "device_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tech_services",
                        to="device_types.devicetype",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tech_service",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-id"],},
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("full_name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-id"],},
        ),
    ]
