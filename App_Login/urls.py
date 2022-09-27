from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.authApiOverview, name='authApi'),
    path('user-list', views.userList, name='userList'),
    path('user/create', views.userCreate, name='userCreate'),

    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout', views.logout, name='userlogout'),
]