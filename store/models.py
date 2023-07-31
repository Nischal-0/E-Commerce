from django.db import models

# Create your models here.

class Category(models.Model):
   name=models.CharField(max_length=255) 

   def __str__(self) -> str:
      return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=5)
    quantity=models.IntegerField(default=0)
    
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    
    def __str__(self) -> str:
      return self.name
   
class Customer(models.Model):
   
   PREMIUM_MEMBER = 'P'
   GOLD_MEMBER = 'G'
   SILVER_MEMBER = 'S'
   BRONZE_MEMBER = 'B'
   
   MEMBERSHIP =[
      (PREMIUM_MEMBER,'Premium'),
      (GOLD_MEMBER,'Gold'),
      (SILVER_MEMBER,'Silver'),
      (BRONZE_MEMBER,'Bronze'),
   ]
   
   firstname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=100) 
   contact = models.IntegerField()
   membership=models.CharField(choices=MEMBERSHIP,default='BRONZE_MEMBER',max_length=1)
   
   def __str__(self) -> str:
      return self.firstname
   
class Address(models.Model):
   customer = models.OneToOneField('Customer',on_delete=models.CASCADE)
   street_name = models.CharField(max_length=100)
   tole_name = models.CharField(max_length=100)
   
   