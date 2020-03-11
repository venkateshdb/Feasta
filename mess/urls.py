from django.urls import path
from mess.views import MessApiView, MessApiViewDetail

urlpatterns  = [
    path('get_mess/', MessApiView.as_view(), name="mess-api-view"),
    path('get_mess/<str:id>/', MessApiViewDetail.as_view())
]