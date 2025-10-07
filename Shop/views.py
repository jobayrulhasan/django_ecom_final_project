from django.shortcuts import render

# Create your views here.
def show_home_page(request):
    return render(request, 'Shop/home.html')