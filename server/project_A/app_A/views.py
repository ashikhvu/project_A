from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import APIViews
# from rest_framework.permision_classes import isAdminUser,AllowAny,isAuthenticated
from .serializers import *
from .models import *
from rest_framework.decorators import api_view

# class ProductHomePage(APIViews):
@api_view(['GET'])
def ProductHomePage(request):
    all_products = Products.objects.all()
    serializers = ProductSerializers(all_products,many=True)
    return Response(serializers.data)


