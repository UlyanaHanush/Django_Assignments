from django.db import models


# Create your models here.

class Beautiful(models.Model):
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
