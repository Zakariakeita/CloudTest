from django.db import models

# Create your models here.
class Participant(models.Model):
    
    nom= models.CharField(max_length=70)
    prenom= models.CharField(max_length=70)
    numero= models.CharField(max_length=70)
    email= models.CharField(max_length=70)
    dateInscription= models.DateField()

