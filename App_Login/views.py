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

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
		
        if request.user.role_id == 999:
            return True
        else:
            return False
    

@api_view(['GET'])
def authApiOverview(request):
	api_urls = {
		'Test':'/test/'
	}

	return Response(api_urls)

@api_view(['GET'])
def userList(request):
	# permission_classes = (permissions.IsAuthenticated,)
	# authentication_classes = [JWTAuthentication, TokenAuthentication] 
	authentication_classes = [JWTAuthentication, TokenAuthentication] 
	permission_classes = [IsAuthenticated, CustomPermission]
	user = User.objects.all().order_by('-id')
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
   
	return Response(serializer.data)

