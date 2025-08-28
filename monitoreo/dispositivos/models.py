from django.db import models


# Create your models here.
class Dispositivos(models.Model):
    nombre = models.CharField(max_length=100)
    consumo_maximo = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
