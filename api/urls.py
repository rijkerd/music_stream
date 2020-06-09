from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView


class TestTemplate(TemplateView):
    template_name = "home.html"


urlpatterns = [
    path('', TestTemplate.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path('', include('artist.urls')),
]
