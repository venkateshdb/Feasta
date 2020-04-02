from django.contrib import messages
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Profile
from .serializers import ProfileSerializer
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
# Create your views here.


class RegView(TemplateView):
    template_name = 'register.html'


# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         phone_no = request.POST['phone_no']
#         address = request.POST['address']
#         location = request.POST['location']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2 :
#             if Profile.objects.filter(email = email).exists():
#                 messages.info(' Email already Taken! ')
#                 return redirect('/register')
#             elif Profile.objects.filter(phone_no = phone_no).exists():
#                 messages.info(' Contact  already Taken! ')
#                 return redirect('/register')
#             else :
#                 profile = Profile.objects.create_user(email= email, phone_no= phone_no, password=password1,
#                     is_shop= False, is_user= True, location = location, address = address,
#                     first_name= first_name, last_name= last_name
#                 )
#                 profile.save()
#                 print('User Created!')
#                 return redirect('/')

#         else :
#             messages.info(' Password not Matching ')
#             return redirect('/register')
#     else:
#         return render(request, 'register.html')


class UserApiView(viewsets.ModelViewSet):
    queryset = Profile.objects
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data = request.data)
        dummy = {}
        if serializer.is_valid():
            account = serializer.save()
            dummy['response']  = "succesfully registered a new user."
            dummy['contact']  = account.phone_no
            dummy['email']  = account.email
            token = Token.objects.get(user = account).key
            dummy['token'] = token
            return Response(dummy,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id):
        # Method: GET
        # Return data about particular mess
        queryset = self.get_detail(id)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        # Method : PUT
        # Update a record
        queryset = self.get_detail(id)
        serializer = ProfileSerializer(queryset, data=request.data, partial=True)
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

    def get_detail(self, mess_id):
        try:
            return Profile.objects.get(id=mess_id)
        except Profile.DoesNotExist:
            raise Http404

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            Profile.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status= status.HTTP_201_CREATED)

        return Response({
            'status' : 'Bad Request',
            'message' : 'Account could not br created with received data.'
        }, status= status.HTTP_404_BAD_REQUEST)