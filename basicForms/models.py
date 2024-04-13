from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
