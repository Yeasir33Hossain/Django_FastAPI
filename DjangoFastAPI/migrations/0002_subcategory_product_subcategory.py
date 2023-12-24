# Generated by Django 5.0 on 2023-12-24 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DjangoFastAPI", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="DjangoFastAPI.subcategory",
            ),
        ),
    ]
