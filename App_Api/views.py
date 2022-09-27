from pickle import NONE
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
# from rest_framework import permissions

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from urllib.request import urlopen
import requests
import json

from .serializers import ProductSerializer, WeatherSerializer

from App_Api.models import Product, Weather

# from App_Api import serializers


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
		
        if request.user.role_id == 999:
            return True
        else:
            return False


def home(request):
    api_key = 'a826261c9ed6ee2652bc1f92e2f0c9ca'
    if request.method == "GET":
        url = 'http://ipinfo.io/json'
        res = urlopen(url)
        data = json.load(res)
        loc = data["city"]
        if(loc == 'Chattogram'):
            city ='Chittagong'
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        # weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
        print(weather_data.json())
        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            temp = round(weather_data.json()['main']['temp'])
            ctemp = ((temp-32)*5/9)
            print(ctemp)
            weather = Weather.objects.all()
            own_weather = 2  # normal
            for w in weather:
                if(ctemp >= w.low_range and ctemp <= w.high_range ):
                    own_weather = w.id
                    break
            print(own_weather)
            weather_product = Product.objects.filter(weather_type=own_weather)
            serailizer = ProductSerializer(weather_product, many=True)
            return JsonResponse(serailizer.data, safe=False)

@csrf_exempt
def product(request):
    if request.method == "GET":
        product = Product.objects.all()
        serailizer = ProductSerializer(product, many=True)
        return JsonResponse(serailizer.data, safe=False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return JsonResponse({
                "Message": "Product added successfully",
                
                "Product": serializer.data}, status=status.HTTP_201_CREATED
                )

        return JsonResponse({"Errors": "sorry product is not added!"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def product_details(request, id):
    try:
        instance = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse( {"error": "Given Product object not found."}, status=404)

    if request.method == "GET":
        serailizer = ProductSerializer(instance)
        return JsonResponse(serailizer.data)

    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = ProductSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=200)
            return JsonResponse({
                "Message": "Product updated successfully",
                
                "Product": serializer.data}, status=status.HTTP_201_CREATED
                )

        return JsonResponse({"Errors": "sorry product has not updated!"}, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == "DELETE":
        instance.delete()
        # return HttpResponse(status=204)
        return JsonResponse({
            "Message": "Product Deleted successfully"}, status=204
            )


def product_search_title(request, slug):
    print("search title")
    try:
        # instance = Product.objects.get(id=id)
        result = Product.objects.filter(name__icontains=slug)
        print(result)
    except Product.DoesNotExist as e:
        return JsonResponse( {"error": "Given Product object not found."}, status=404)

    if request.method == "GET":
        serailizer = ProductSerializer(result, many=True)
        return JsonResponse(serailizer.data, safe=False)

@csrf_exempt
def product_list_weather(request,slug):
    slug = slug.capitalize()
    try:
        instance = Weather.objects.get(title=slug)
    except Weather.DoesNotExist as e:
        return JsonResponse( {"error": "Given Weather object not found."}, status=404)

    if request.method == "GET":
        weather_product = Product.objects.filter(weather_type=instance.id)
        serailizer = ProductSerializer(weather_product, many=True)
        return JsonResponse(serailizer.data, safe=False)
        
@csrf_exempt
def weather(request):
    if request.method == "GET":
        weather = Weather.objects.all()
        serailizer = WeatherSerializer(weather, many=True)
        return JsonResponse(serailizer.data, safe=False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = WeatherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "Message": "Weather added successfully",
                
                "Product": serializer.data}, status=status.HTTP_201_CREATED
                )

        return JsonResponse({"Errors": "sorry weather is not added!"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def weather_details(request, slug):
    slug = slug.capitalize()
    try:
        instance = Weather.objects.get(title=slug)
    except Weather.DoesNotExist as e:
        return JsonResponse( {"error": "Given Weather object not found."}, status=404)

    if request.method == "GET":
        serailizer = WeatherSerializer(instance)
        return JsonResponse(serailizer.data)

    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = WeatherSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=200)
            return JsonResponse({
                "Message": "Weather updated successfully",
                
                "Product": serializer.data}, status=status.HTTP_201_CREATED
                )

        return JsonResponse({"Errors": "sorry weather is not updated!"}, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == "DELETE":
        instance.delete()
        return JsonResponse({
            "Message": "Weather Deleted successfully"}, status=204
            )