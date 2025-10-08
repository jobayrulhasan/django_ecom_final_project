from django.shortcuts import render

# Create your views here.
def show_home_page(request):
    return render(request, 'Shop/home.html')

def show_shop_page(request):
    return render(request, 'Shop/shop.html')

def show_single_page(request):
    return render(request, 'Shop/single.html')