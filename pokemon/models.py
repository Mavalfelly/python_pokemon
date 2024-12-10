from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pokemon(models.Model):
    poke_type=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pokemon')
        #on_delete=models.CASCADE, null=True, blank=True,
        #when a user is deleted, delete everything the authored

   