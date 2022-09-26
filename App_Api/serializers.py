from rest_framework import serializers
from App_Api.models import Product, Weather

class WeatherSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Weather
		fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
	print("ddd")
	weather_type = WeatherSerializer(many=False)
	class Meta:
		model = Product
		fields ='__all__'
		fields = [
			"id",
			"name",
			# "weather_type",
			"price",
			"weather_type"
		]
	# def create(self, validated_data):
	# 	if "id" in validated_data.keys():
	# 		print("id exist")
	# 		return 
	# 	product = Product.objects.create(**validated_data)
	# 	return product