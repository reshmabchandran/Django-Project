# Generated by Django 5.0 on 2024-01-10 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("real_estate_management_app", "0003_propertydetails_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propertydetails",
            name="locaton",
            field=models.CharField(max_length=130),
        ),
        migrations.CreateModel(
            name="UnitDetails",
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
                ("pname", models.CharField(max_length=100)),
                ("uname", models.EmailField(max_length=100)),
                ("rent_cost", models.CharField(max_length=13)),
                ("types", models.CharField(max_length=500)),
                ("status", models.CharField(max_length=10)),
                (
                    "properti",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="real_estate_management_app.propertydetails",
                    ),
                ),
            ],
        ),
    ]
