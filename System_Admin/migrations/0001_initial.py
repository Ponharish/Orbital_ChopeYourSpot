# Generated by Django 4.2.13 on 2024-06-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="paymenthistorydump",
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
                ("domain", models.CharField(max_length=30)),
                ("PaymentReference", models.CharField(max_length=30)),
            ],
        ),
    ]
