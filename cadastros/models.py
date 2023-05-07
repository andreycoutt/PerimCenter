from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=250, verbose_name="endereço")

    def __str__(self):
        return "Nome: {} - CPF: {} - Telefone: {} - Endereço: {}".format(self.nome, self.cpf, self.telefone, self.endereco)