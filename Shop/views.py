from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Product

# Create your views here.
def show_home_page(request):
    accessories = Product.objects.filter(category = 'Acc')
    electronics_computer = Product.objects.filter(category = 'EC')
    laptops_desktops = Product.objects.filter(category = 'LD')
    mobiles_tablets = Product.objects.filter(category = 'MT')
    SmartPhone_smart_TV = Product.objects.filter(category = 'SSTV')
    all_products = Product.objects.all()
    
    new_arrival = Product.objects.filter(product_status = 'New')
    sale_product = Product.objects.filter(product_status = 'Sale')
    feature_product = Product.objects.filter(product_status = 'Feature')
    top_salling_product = Product.objects.filter(product_status = 'Top Selling')
    
    return render(request, 'Shop/home.html', {'accessories': accessories, 'electronics_computer':electronics_computer, 'laptops_desktops':laptops_desktops, 'mobiles_tablets':mobiles_tablets, 'SmartPhone_smart_TV': SmartPhone_smart_TV, 'all_products':all_products, 'new_arrival': new_arrival, 'sale_product': sale_product, 'feature_product': feature_product, 'top_salling_product': top_salling_product})


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
            return render(request, 'Shop/userregistration.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'Shop/userregistration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'Shop/userregistration.html')

        user = User(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        #return redirect('login')

    return render(request, 'Shop/userregistration.html')

#user login
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Login successful!")
            return redirect('/')  # redirect to your home/dashboard page
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'Shop/login.html')

# user logout
def user_logout(request):
    logout(request)
    return redirect('/')

#change password
@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Check old password
        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return redirect('change_password')

        # Confirm new passwords match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            return redirect('change_password')

        # Validate new password strength using Django's validators
        try:
            validate_password(new_password, user=request.user)
        except ValidationError as e:
            # e.messages is a list of human-friendly messages
            for msg in e.messages:
                messages.error(request, msg)
            return redirect('change_password')

        # Set new password (securely hashes)
        request.user.set_password(new_password)
        request.user.save()

        # Keep the user logged in after password change
        update_session_auth_hash(request, request.user)

        # messages.success(request, 'Your password has been changed successfully.')
        return redirect('/')

    # GET request -> show form
    return render(request, 'Shop/password_change.html')
