from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegView, UserApiView

urlpatterns = [
    path('', RegView.as_view(), name="register"),
    path('login', obtain_auth_token, name ="Api Login"),
    path('get-user/', UserApiView.as_view({'get': 'get',
                                         'post': 'post'}), name="UserRegister-api-view"),
    path('get-user/<str:id>/', UserApiView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
