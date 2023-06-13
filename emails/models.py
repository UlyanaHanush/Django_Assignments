from django.db import models

# Create your models here.
class Web(models.Model):
    news_headline = models.CharField(max_length=255)
    news_website = models.CharField(max_length=255)
    date = models.DateField()