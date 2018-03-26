from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    tel_fixo = models.CharField(max_length=12)
    cel = models.CharField(max_length=13)