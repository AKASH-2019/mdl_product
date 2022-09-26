from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     # TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('product', views.product, name='product'),
    path('product/details/<id>', views.product_details, name='productDetails'),
    path('product/list/<slug>', views.product_list_weather, name='productListWeather'),
    
    # path('product-list', views.productList, name='productList'),

    path('weather', views.weather, name='weather'),
    path('weather/details/<slug>', views.weather_details, name='weatherDetails'),
]