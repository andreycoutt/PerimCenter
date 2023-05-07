from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=250, verbose_name="endereço")

    def __str__(self):
        return "Nome: {} - CPF: {} - Telefone: {} - Endereço: {}".format(self.nome, self.cpf, self.telefone, self.endereco)
    

class Entrega(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=250, verbose_name="endereço")
    caixas = models.IntegerField()
    volumeextra = models.CharField(max_length=150, verbose_name='Volume Extra')
    nomeembalador = models.CharField(max_length=50, verbose_name='Nome do Embalador')
    datacompra = models.DateField('data', null=True, blank=True)
    datahoraentrega = models.DateTimeField('data', null=True, blank=True)

    
    
    def __str__(self): 
        return "Nome: {} - Endereço: {} - Caixas: {} - Volume Extra: {} - Nome do Embalador: {} - Data de Compra: {} - Data de Entrega: {}".format(self.nome, self.endereco, self.caixas, self.volumeextra, self.nomeembalador, self.datacompra, self.datahoraentrega)