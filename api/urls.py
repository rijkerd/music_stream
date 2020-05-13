from django.urls import include, path
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path('', include('music.urls'))
]
