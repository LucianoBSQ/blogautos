from django.db import models


class Diseñadores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    
    def __str__(self):
        return (f"{self.apellido} {self.nombre}")

class Empresas(models.Model):
    nombre= models.CharField(max_length=30)
    ubicacion= models.CharField(max_length=30)
    
    def __str__(self):
        return (f"{self.nombre}")

class Diseños (models.Model):
    modelo= models.CharField(max_length=30, null=True) 
    autor= models.CharField(max_length=30,null=True) 
    
    def __str__(self):
        return (f"{self.modelo}")
       


