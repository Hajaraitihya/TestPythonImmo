from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model



class Programme(models.Model):
    name= models.CharField(max_length=200)
    actif = models.BooleanField()
    
class Caracteristique(models.Model):
    description=models.CharField(max_length=200)
    
class Appartement(models.Model):
    prix =models.FloatField()
    surface =models.FloatField()
    nombre_piece = models.IntegerField()
    caracteristiques = models.ManyToManyField(Caracteristique, related_name='descriptions')
    Id_programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
