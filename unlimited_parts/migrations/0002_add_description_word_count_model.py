# Generated by Django 4.1.5 on 2023-01-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited_parts", "0001_add_part_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="DescriptionWordCount",
            fields=[
                (
                    "word",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("count", models.IntegerField(default=0)),
            ],
        ),
    ]