from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shop import views


urlpatterns = [
    path('', views.show_home_page, name="home"),
    path('shop/', views.show_shop_page, name = 'shop_page'),
     path('single/', views.show_single_page, name = 'single_page'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)