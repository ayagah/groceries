from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product (models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    stock=models.IntegerField()
    available=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name