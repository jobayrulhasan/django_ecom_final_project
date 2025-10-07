from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Shop import views


urlpatterns = [
    path('', views.show_home_page, name="home"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)