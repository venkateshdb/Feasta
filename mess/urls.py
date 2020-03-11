from django.urls import path
from mess.views import MessApiView

urlpatterns  = [
    path('get_mess/', MessApiView.as_view(), name="mess-api-view")
]