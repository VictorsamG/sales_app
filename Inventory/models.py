from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100,default="All",null=True,blank=True)
    engine_type= models.CharField(max_length=100,default='All',null=True,blank=True)
    stock_balance = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    product_image = models.ImageField(upload_to='static/images/',null=True,blank=True)
    
    def __str__(self):
        return(f"{self.product_name} | {self.part_number}")
    
    @property

    def stock_valuation(self):
        return self.stock_balance*self.unit_cost