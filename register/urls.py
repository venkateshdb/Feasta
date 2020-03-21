from django.urls import path
from .views import RegView, UserLogin, ShopLogin

urlpatterns = [
    path('', RegView.as_view(), name="register"),
    path('get-user/', UserLogin.as_view({'get': 'get',
                                         'post': 'post'}), name="UserRegister-api-view"),
    path('get-user/<str:id>/', UserLogin.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('get-shop/', ShopLogin.as_view({'get': 'get',
                                         'post': 'post'}), name="ShopRegister-api-view"),
    path('get-shop/<str:id>/', ShopLogin.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
