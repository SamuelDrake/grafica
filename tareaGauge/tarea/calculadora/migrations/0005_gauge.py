# Generated by Django 4.1.7 on 2023-04-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0004_usuario_partidas"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gauge",
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
                ("user_name", models.CharField(max_length=20)),
                ("puntaje", models.IntegerField()),
            ],
        ),
    ]