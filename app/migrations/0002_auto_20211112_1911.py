# Generated by Django 3.2.9 on 2021-11-12 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enquete",
            name="opcao",
        ),
        migrations.RemoveField(
            model_name="enquete",
            name="votos",
        ),
        migrations.CreateModel(
            name="Resposta",
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
                ("opcao", models.CharField(max_length=200)),
                ("votos", models.IntegerField(default=0)),
                (
                    "enquete_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.enquete"
                    ),
                ),
            ],
        ),
    ]
