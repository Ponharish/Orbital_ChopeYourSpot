# Generated by Django 4.2.13 on 2024-05-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="users",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30)),
                ("domain", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
