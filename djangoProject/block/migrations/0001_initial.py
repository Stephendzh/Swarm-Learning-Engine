# Generated by Django 4.2.7 on 2024-02-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Block",
            fields=[
                (
                    "index",
                    models.IntegerField(
                        max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("transactions", models.TextField()),
                ("nonce", models.IntegerField()),
                ("previous_hash", models.TextField()),
            ],
        ),
    ]