from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shop import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.show_home_page, name="home"),
    path('shop/', views.show_shop_page, name = 'shop_page'),
    path('single/', views.show_single_page, name = 'single_page'),
    
    #user registratin
    path('registration/', views.registration, name = 'user_registration'),
    #user login
    path('login/', views.login_view, name = 'user_login'),
    #logout
    path('logout/', views.user_logout, name='userLogout'),
    # Password change
    path('change-password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)