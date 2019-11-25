from django.urls import include, path
from rest_framework.schemas import get_schema_view
from music import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('song/<int:pk>', views.SongDetail.as_view(), name='song-detail'),
    path('albums/', views.AlbumList.as_view(), name='album-list'),
    path('album/<int:pk>', views.AlbumDetails.as_view(), name='album-detail'),
    # path('songs/', MusicListView.as_view({'get': 'list'})),
    # path('album/', AlbumListView.as_view({'get': 'list'})),
]
