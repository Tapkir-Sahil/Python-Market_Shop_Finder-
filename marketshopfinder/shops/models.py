from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ShopVariety(models.Model):
    SHOP_TYPE_LOC=[
        ('PU','Pune'),
        ('MU','Mumbai'),
        ('NA','Nagpur'),
        ('KO','Kokan'),
        ('SA','Satara'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='typeshop/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=9,choices=SHOP_TYPE_LOC,default='PU')
    description=models.TextField()
    def __str__(self):
     return self.name
    class Meta:
        verbose_name = "Shop Variety"
        verbose_name_plural = "Shop Varieties"

#one to many
class Shop_review(models.Model):
   shop=models.ForeignKey(ShopVariety,on_delete=models.CASCADE,related_name='reviews')
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   rating=models.IntegerField()
   date_added=models.DateField(default=timezone.now)

   def __str__(self):
      return f'{self.user.username} review for {self.shop.name}'


#many to many
class Store(models.Model):
   name=models.CharField(max_length=100)
   location=models.CharField(max_length=100)
   shopvarities=models.ManyToManyField(ShopVariety,related_name='stores')

   def __str__(self):
      return self.name

#one to one

class Cerificate(models.Model):
   shop=models.OneToOneField(ShopVariety,on_delete=models.CASCADE,related_name='certificate')
   Cnumber=models.CharField(max_length=50)
   issued_date=models.DateTimeField(default=timezone.now)
   valid_until=models.DateField()

   def __str__(self):
      return f'Certifate for {self.shop.name}'