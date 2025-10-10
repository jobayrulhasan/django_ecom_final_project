from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def show_home_page(request):
    return render(request, 'Shop/home.html')

def show_shop_page(request):
    return render(request, 'Shop/shop.html')

def show_single_page(request):
    return render(request, 'Shop/single.html')

# customer registration
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('Shop/userregistration.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('Shop/userregistration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('Shop/userregistration.html')

        user = User(
            username=username,
            email=email,
            password=make_password(password)  # securely hash password
        )
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('Shop/login.html')

    return render(request, 'Shop/userregistration.html')


def login(request):
    return render(request, 'Shop/login.html')