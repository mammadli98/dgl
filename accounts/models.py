from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    name_der_praxis = models.CharField(max_length=30,null=True)
    fachrichtung = models.CharField(max_length=30,null=True)
    strasse = models.CharField(max_length=30,null=True)
    strasse_nr = models.IntegerField(null=True)
    postleitzahl  = models.IntegerField(null=True)

    ansprechpartner = models.CharField(max_length=30,null=True)
    mitarbeiter = models.IntegerField(null=True)
    arzt = models.IntegerField(null=True)
    groese_praxis = models.IntegerField(null=True)
    raume = models.IntegerField(null=True)
    anmerkungen = models.TextField(null=True)



    def __str__(self):
        return self.username

