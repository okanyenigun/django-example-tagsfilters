from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=100)
    is_new = models.BooleanField()
    age = models.IntegerField()
    engine = models.CharField(max_length=100)