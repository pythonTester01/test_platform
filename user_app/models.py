from django.db import models

# Create your models here.
class projectTable(models.Model):
    title = models.CharField(max_length=2000)
    a = models.CharField(max_length=2000)
    b = models.CharField(max_length=2000)

