from django.db import models
import uuid

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.customer_name