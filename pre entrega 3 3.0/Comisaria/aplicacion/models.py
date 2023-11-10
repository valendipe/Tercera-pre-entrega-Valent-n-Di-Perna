from django.db import models

# Create your models here.
class Comisaria(models.Model):
    nombre= models.CharField(max_length=256)
    numero= models.IntegerField()
    def __str__(self):
        return f"{self.nombre} ({self.numero})"
    
    
class Policia(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"{self.apellido} {self.nombre}"
class Detenido(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    motivo_de_detencion=models.TextField()
    dni= models.IntegerField(null=True)
    fecha_de_nacimiento= models.DateField(null=True)
    def __str__(self):
        return f"{self.apellido} {self.nombre}, nacido el {self.fecha_de_nacimiento}"