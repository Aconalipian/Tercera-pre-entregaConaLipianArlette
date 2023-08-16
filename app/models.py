from django.db import models

class pelicula(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_estreno= models.DateField()
    productora = models.CharField(max_length=50)
    genero = models.CharField(max_length=60)

    class Meta:
        verbose_name ="pelicula"
        verbose_name_plural = "peliculas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}, {self.fecha_estreno}, {self.productora}, {self.genero}"


class director(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    class Meta:
        verbose_name ="director"
        verbose_name_plural = "directores"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre},  {self.nacionalidad}"

class productoras(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    class Meta:
        verbose_name ="productora"
        verbose_name_plural = "productoras"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}, {self.pais}"

