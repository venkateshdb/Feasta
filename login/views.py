from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import serializers
from register.models import User, ShopOwner
# Create your views here.

# class UserSession(serializers.ModelSerializer):
#     model = User.objects.only('username', 'email', 'phone', 'password', 'last_login', 'is_active', 'date_created')
#     fields = "__all__"

class LoginView(TemplateView):
    template_name = 'login.html'

# class LoginUser(viewsets.ModelViewSet):
#     queryset = User.objects
#     serializer_class = UserSession

#     def get(self, request):
#         # method: GET
#         # Return about User
#         queryset = User.objects.all().only('username', 'email', 'phone', 'password', 'last_login', 'is_active', 'date_created')
#         serializer = UserSession(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         pass