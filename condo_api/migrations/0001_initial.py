# Generated by Django 5.0.4 on 2024-04-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apartamento",
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
                ("num_do_apto", models.IntegerField(default=0)),
                ("andar", models.IntegerField(default=0)),
                ("lista_de_tags", models.CharField(default="", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Condominio",
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
                ("nome", models.CharField(default="", max_length=200)),
                ("cnpj", models.CharField(default="", max_length=14)),
                ("endereco", models.CharField(default="", max_length=200)),
                ("cep", models.CharField(default="", max_length=9)),
                ("num_blocos", models.IntegerField(default=1)),
                ("num_aptos", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="ControleDeAcesso",
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
                ("num_tag", models.IntegerField(default=1)),
                (
                    "data_hora",
                    models.DateTimeField(
                        default="", verbose_name="Data/hora do acesso"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("num_tag", models.IntegerField(default=1)),
                (
                    "num_sequencial",
                    models.IntegerField(
                        default=0, verbose_name="Numero identificador no condomínio"
                    ),
                ),
            ],
        ),
    ]
