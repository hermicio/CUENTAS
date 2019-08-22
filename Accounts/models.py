
from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Accounts(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    account = models.CharField(max_length=200)
    date = models.DateTimeField('Fecha de Creacion')

class Mov(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    date = models.DateTimeField('Fecha Movimiento')