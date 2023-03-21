# Generated by Django 4.1.7 on 2023-03-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=20, null=True)),
                ("email", models.CharField(max_length=20, null=True)),
                ("phone_number", models.CharField(max_length=20, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
