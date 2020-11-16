from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView


class TestTemplate(TemplateView):
    template_name = "home.html"


urlpatterns = [
    path('', TestTemplate.as_view()),
    path('', include('users.urls')),
    path('', include('artist.urls')),
    path('', include('album.urls')),
    path('', include('genre.urls')),
    path('', include('track.urls')),
]
