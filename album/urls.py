from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet

album_list = AlbumViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

album_detail = AlbumViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = router.urls
