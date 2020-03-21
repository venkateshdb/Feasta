from django.contrib import admin
from django.urls import path, include

# remove in production
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def api(prefix=None):
    """
    :param prefix:
    :return: Base url for API
    """
    if prefix is None:
        return "api/v1/"
    else:
        return "api/v1/{}".format(prefix)


urlpatterns = [
    path('', include('mess.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path(api(), include('mess.urls')),
    url(r'^(?P<path>.*)/', include('mess.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
]
