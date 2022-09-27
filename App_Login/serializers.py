from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields ='__all__'
		fields = [
			"id",
			"email",
			"password"
		]



