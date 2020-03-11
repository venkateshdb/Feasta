from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mess.serializer import MessSerializer
from mess.models import Mess, Menu, Price
from django.http import Http404


class MessApiView(APIView):
    """
    This view will return data about mess
    """

    def get(self, request):
        # method: GET
        # Return about Mess
        queryset = Mess.objects.all()
        serializer = MessSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # method: POST
        # Add details about Mess
        serializer = MessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessApiViewDetail(APIView):
    """
    This view will return data about a give mess
    ,update and delete the data
    """

    def get_detail(self, id):
        try:
            return Mess.objects.get(pk=id)
        except Mess.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_detail(id)
        serializer = MessSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_detail(id)
        serializer = MessSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = self.get_detail(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
