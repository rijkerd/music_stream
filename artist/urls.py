from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet

artist_list = ArtistViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

artist_detail = ArtistViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artist')

urlpatterns = router.urls
