from django.db import models

# Create your models here.

class my_num(models.Model):
    # data
    dat = models.IntegerField()
    char = models.CharField(max_length=16, default='null')