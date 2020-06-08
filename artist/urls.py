from django.urls import path
from .views import ArtistList, ArtistDetail

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('artists/<id>', ArtistDetail.as_view(), name='artist-detail'),
]
