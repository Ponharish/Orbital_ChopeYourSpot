# Generated by Django 4.2.13 on 2024-07-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("System_Admin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("sender", models.CharField(max_length=30)),
                ("senderdomain", models.CharField(max_length=30)),
                ("receiver", models.CharField(max_length=30)),
                ("receiverdomain", models.CharField(max_length=30)),
                ("subject", models.TextField()),
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
