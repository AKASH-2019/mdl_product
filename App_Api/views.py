from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
# from rest_framework import permissions

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer

from App_Login.models import User


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
		
        if request.user.role_id == 999:
            return True
        else:
            return False
    


@api_view(['GET'])
def productList(request):
	authentication_classes = [JWTAuthentication, TokenAuthentication] 
	permission_classes = [IsAuthenticated, CustomPermission]
	user = User.objects.all().order_by('-id')
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)