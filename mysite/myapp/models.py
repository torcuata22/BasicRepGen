from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()



