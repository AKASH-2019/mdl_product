from rest_framework import serializers
from App_Api.models import Product, Weather

class WeatherSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Weather
		fields ='__all__'

class ProductInsertSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
	print("ddd")
	weather_type = WeatherSerializer(many=False)
	class Meta:
		model = Product
		# fields ='__all__'
		fields = [
			"id",
			"name",
			"price",
			"quantity",
			"weather_type"
		]
