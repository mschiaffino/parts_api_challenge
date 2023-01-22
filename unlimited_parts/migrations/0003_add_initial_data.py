# Generated by Django 4.1.5 on 2023-01-21 22:56

import sys

from django.db import migrations, models
from unlimited_parts.models import Part


def insert_data(app, schema_editor):
    Part(
        name="Heavy coil",
        sku="SDJDDH8223DHJ",
        description="Tightly wound nickel-gravy alloy spring",
        weight_ounces=22,
        is_active=1,
    ).save()
    Part(
        name="Reverse lever",
        sku="DCMM39823DSJD",
        description="Attached to provide inverse leverage",
        weight_ounces=9,
        is_active=0,
    ).save()
    Part(
        name="Macrochip",
        sku="OWDD823011DJSD",
        description="Used for heavy-load computing",
        weight_ounces=2,
        is_active=1,
    ).save()


class Migration(migrations.Migration):
    dependencies = [
        ("unlimited_parts", "0002_add_description_word_count_model"),
    ]

    operations = (
        [
            migrations.RunPython(insert_data),
        ]
        # Ignore data insertion when running tests
        if "test" not in sys.argv[1:]
        else []
    )
