from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    decp = models.TextField()


class Person(models.Model):
    name1 = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    decs = models.TextField()


def __str__(self):
    return self.name


def __str__(self):
    return self.name1
