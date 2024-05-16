from django.db import models

class Condominio(models.Model):
    nome = models.CharField(max_length=200, default="")
    cnpj = models.CharField(max_length=19, default="", unique=True)
    endereco = models.CharField(max_length=200, default="")
    cep = models.CharField(max_length=9, default="")
    num_blocos = models.IntegerField(default=1)
    num_aptos = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.nome

class Tag(models.Model):
    num_tag = models.IntegerField(default=1, unique=True)
    num_sequencial = models.IntegerField(
        "Numero identificador no condomínio", default=0
    )
    def __str__(self) -> str:
        return str(self.num_tag)

class Apartamento(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete = models.CASCADE)
    bloco = models.IntegerField(default=0)
    num_do_apto = models.IntegerField(default=0)
    andar = models.IntegerField(default=0)
    tags = models.CharField(max_length=200, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['condominio', 'bloco', 'num_do_apto'], name='unique_apto'),
        ]    
    def __str__(self) -> str:
        return str(self.num_do_apto)

class ControleDeAcesso(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    data_hora = models.DateTimeField("Data/hora do acesso", default="")