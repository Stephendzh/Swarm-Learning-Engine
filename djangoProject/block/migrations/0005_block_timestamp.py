# Generated by Django 4.2.7 on 2024-03-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("block", "0004_simpleblock"),
    ]

    operations = [
        migrations.AddField(
            model_name="block",
            name="timestamp",
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]