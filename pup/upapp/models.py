from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userpi(models.Model):
    user = models.OneToOneField(User)

    portfoliosite = models.CharField(max_length=100,blank=True)
    profilepic = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
        
