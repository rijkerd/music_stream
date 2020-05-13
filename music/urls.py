from django.urls import path
from music import views

urlpatterns = [
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('song/<int:pk>', views.SongDetail.as_view(), name='song-detail'),
    path('albums/', views.AlbumList.as_view(), name='album-list'),
    path('album/<int:pk>', views.AlbumDetails.as_view(), name='album-detail'),
]
