from django.db import models
from django.utils import timezone

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