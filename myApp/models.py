from django.db import models

class Producto (models.Model):
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen_uno = models.ImageField(upload_to='img1')
    nombre_vendedor = models.CharField(max_length=50)
    telefono = models.IntegerField()
          
    def __str__(self):
        return self.descripcion

