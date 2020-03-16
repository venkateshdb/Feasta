from django.urls import path
from .views import LoginView
urlpatterns = [
    path('',LoginView.as_view(),name = "login"),
    # path('get-user/', LoginUser.as_view({'get': 'get', 'post': 'post'}), name="LoginUser-api-view"),
]