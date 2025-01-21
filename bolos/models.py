from django.db import models




class Bolo(models.Model):
    aniversario = models.CharField(max_length=15)
    texto = models.TextField(max_length=1000)
