from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title='Chat API',
        description='Chat API',
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
    authentication_classes=[JWTAuthentication,],
)

urlpatterns = [
   path('api/docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
