from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ('Acc', 'Accessories'),
    ('EC', 'Electronics & Computer'),
    ('LD', 'Laptops & Desktops'),
    ('MT', 'Mobiles & Tablets'),
    ('SSTV', 'SmartPhone & Smart TV'),
)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    product_image = models.ImageField(upload_to='productimg')
    product_status = models.TextField()

    def __str__(self):
        return str(self.id)
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)