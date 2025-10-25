from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Product, Cart
from django.db.models import Q
from django.http import JsonResponse

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



# best selling page
def show_bestselling_page(request):
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
    
    return render(request, 'Shop/bestseller.html', {'accessories': accessories, 'electronics_computer':electronics_computer, 'laptops_desktops':laptops_desktops, 'mobiles_tablets':mobiles_tablets, 'SmartPhone_smart_TV': SmartPhone_smart_TV, 'all_products':all_products, 'new_arrival': new_arrival, 'sale_product': sale_product, 'feature_product': feature_product, 'top_salling_product': top_salling_product})

# show cart page
def show_cart_page(request):
    return render(request, 'Shop/cart.html')

# show checkout page
def show_cheackout_page(request):
    return render(request, 'Shop/cheackout.html')

# show checkout page
def show_contact_page(request):
    return render(request, 'Shop/contact.html')

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        productDetails = Product.objects.get(pk=pk)
        return render(request, 'Shop/productdetails.html', {'productD': productDetails})
    
# Add to card
def add_to_cart(request):
    userName = request.user
    product_Id = request.GET.get('product_id')
    productTable = Product.objects.get(id = product_Id)
    Cart(user=userName, product = productTable).save()
    return redirect('/cart')



# show cart page
def show_cart_page(request):
    return render(request, 'Shop/cart.html')


# show in cart
# def show_cart(request):
#     if request.user.is_authenticated:
#         username = request.user
#         cart = Cart.objects.filter(user=username)
        
#         shipping_amount = 0
#         amount = 0
        
#         cart_product = [p for p in cart]
        
#         if cart_product:
#             for p in cart_product:
                
    
#              return render(request, 'Shop/cart.html', {'carts': cart})
#     else:   # if cart is empty
#         return render(request, 'Shop/emptycart.html')
    
    
# show in cart
def show_cart(request):
    if request.user.is_authenticated:
        username = request.user
        cart = Cart.objects.filter(user=username)
        amount = 0
        shipping_amount = 0
        cart_product = [p for p in cart]  # no need to filter again

        if cart_product:   # if cart is not empty
            for p in cart_product:
                temp_amount = p.quantity * p.product.discounted_price
                amount += temp_amount
                # condition for shipping
                if amount > 0:
                    shipping_amount = 100
                else:
                    shipping_amount = 0
            total_amount = amount + shipping_amount
            return render(request, 'Shop/cart.html', {
                'carts': cart,
                'totalamount': total_amount,
                'amount': amount,
                'shippingamount':shipping_amount
            })
        else:   # if cart is empty
            return render(request, 'Shop/emptycart.html')
        
        
# plus in cart
def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        amount = 0
        shipping_amount = 100
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        if amount > 0:
            shipping_amount = 100
        else:
            shipping_amount = 0

        totalamount = amount + shipping_amount

        # Add this 👇 line total for current product
        product_total = c.quantity * c.product.discounted_price

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
            'shippingAmount': shipping_amount,
            'productTotal': product_total
        }
        return JsonResponse(data)
