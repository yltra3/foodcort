# Generated by Django 4.1.7 on 2023-03-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0004_mcdonalds"),
    ]

    operations = [
        migrations.AddField(
            model_name="mcdonalds",
            name="name",
            field=models.CharField(default="null", max_length=40),
        ),
        migrations.AddField(
            model_name="mcdonalds",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
