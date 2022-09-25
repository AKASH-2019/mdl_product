from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     # TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('product-list', views.productList, name='productList'),
]