from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mess.serializer import MessSerializer
from mess.models import Mess, Menu, Price


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

    def put(self, request):
        pass

    def delete(self, request):
        pass
