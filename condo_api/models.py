from django.db import models


class Condominio(models.Model):
    nome = models.CharField(max_length=200, default="")
    cnpj = models.CharField(max_length=14, default="")
    endereco = models.CharField(max_length=200, default="")
    cep = models.CharField(max_length=9, default="")
    num_blocos = models.IntegerField(default=1)
    num_aptos = models.IntegerField(default=1)


class Apartamento(models.Model):
    num_do_apto = models.IntegerField(default=0)
    andar = models.IntegerField(default=0)
    lista_de_tags = models.CharField(max_length=200, default="")


class Tag(models.Model):
    num_tag = models.IntegerField(default=1)
    num_sequencial = models.IntegerField(
        "Numero identificador no condomínio", default=0
    )


class ControleDeAcesso(models.Model):
    num_tag = models.IntegerField(default=1)
    data_hora = models.DateTimeField("Data/hora do acesso", default="")
