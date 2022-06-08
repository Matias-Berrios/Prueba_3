from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    sku = models.CharField(max_length=6, primary_key=True, verbose_name='Sku')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion del producto')
    urlimg = models.CharField(max_length=150, verbose_name='Url de la imagen')
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Cantidad de stock')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku
