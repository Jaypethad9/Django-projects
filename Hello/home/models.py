from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()  
    def __str__(self):
        return self.name

class icepops(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default = False)

class Shop(models.Model):
    desc = models.TextField()
    paymentMethod = models.CharField(max_length=122)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField() 