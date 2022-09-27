from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('product', views.product, name='product'),
    path('product/create', views.productCreate, name='productCreate'),
    path('product/details/<id>', views.product_details, name='productDetails'),
    path('product/weather/<slug>', views.product_list_weather, name='productListWeather'),
    path('product/<slug>', views.product_search_title, name='productSearchTitle'),

    path('weather', views.weather, name='weather'),
    path('weather/details/<slug>', views.weather_details, name='weatherDetails'),

    path('home', views.home, name='home'),
]