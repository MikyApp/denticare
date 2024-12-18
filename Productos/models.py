from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sku = models.CharField(max_length=10)
    precio = models.FloatField()
    marca = models.CharField(max_length=20)
    codigo_interno = models.CharField(max_length=10)
    presentacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen_producto = models.ImageField(upload_to='productos', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre

