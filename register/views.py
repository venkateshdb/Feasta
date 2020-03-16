from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import UserSerializers, ShopSerializers
from .models import User, ShopOwner
# Create your views here.


class RegView(TemplateView):
    template_name = 'register.html'

class UserLogin(viewsets.ModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializers

    def get(self, request):
        # method: GET
        # Return about User
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # method: POST
        # Add details about User
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    """
    This view will return data about a give User
    ,update and delete the data
    """

    def retrieve(self, request, id):
        # Method: GET
        # Return data about particular User
        queryset = self.get_detail(id)
        serializer = UserSerializers(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        # Method : PUT
        # Update a record
        queryset = self.get_detail(id)
        serializer = UserSerializers(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        # Method: DELETE
        # Delete a record
        queryset = self.get_detail(id)
        queryset.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, User_id):
        try:
            return User.objects.get(id=User_id)
        except User.DoesNotExist:
            raise Http404

class ShopLogin(viewsets.ModelViewSet):
    queryset = ShopOwner.objects
    serializer_class = ShopSerializers

    def get(self, request):
        # method: GET
        # Return about ShopOwner
        queryset = ShopOwner.objects.all()
        serializer = ShopSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # method: POST
        # Add details about ShopOwner
        serializer = ShopSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    """
    This view will return data about a give ShopOwner
    ,update and delete the data
    """

    def retrieve(self, request, id):
        # Method: GET
        # Return data about particular Shop
        queryset = self.get_detail(id)
        serializer = ShopSerializers(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        # Method : PUT
        # Update a record
        queryset = self.get_detail(id)
        serializer = ShopSerializers(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        # Method: DELETE
        # Delete a record
        queryset = self.get_detail(id)
        queryset.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, User_id):
        try:
            return ShopOwner.objects.get(id=User_id)
        except ShopOwner.DoesNotExist:
            raise Http404