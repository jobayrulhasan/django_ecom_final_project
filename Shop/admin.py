from django.contrib import admin
from .models import(
    Product,
    Cart
)

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','selling_price','discounted_price','description','brand','category','product_image', 'product_status']
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product','quantity']
    
