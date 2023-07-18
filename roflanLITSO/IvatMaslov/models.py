from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

class rap(models.Model):
    type = models.CharField(max_length=200)
    borncounrty = models.CharField(max_length=200)

class info(models.Model):
    opred = models.CharField(max_length=300)
    history = models.CharField(max_length=1000)

class look(models.Model):
    types = models.CharField(max_length=70)

class famous(models.Model):
    Person = models.CharField(max_length=100)
    squade = models.CharField(max_length=100)