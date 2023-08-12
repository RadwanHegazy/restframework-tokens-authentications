from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class NameModel (models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self) : 
        return f'{self.name}'



@receiver(post_save,sender=User)
def CreateTokenForUser (created,instance,**args) : 
    if created : 
        Token.objects.create(user = instance)