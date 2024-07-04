from django.db import models
import uuid

# Create your models here.
#Al hablar de models estamos hablando de la tabla de la base de datos 
#Hay que hacer un python manage.py makemigrations para que se vea que los cambios estan correctos
#despues un manage.py migrate
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField() #cajita para escribir
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    receta = models.TextField() #al generar nuevo atributo del modelo se debe hacer migracion

    def __str__(self): #hace que se vea el nombre del flan en vez de object
        return f"{self.name}"
    

    

    
    
    


    
