from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet

track_list = TrackViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

track_detail = TrackViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='track')

urlpatterns = router.urls
