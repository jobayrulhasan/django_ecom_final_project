from django.contrib import admin
from .models import(
    Product
)

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','selling_price','discounted_price','description','brand','category','product_image', 'product_status']
    
