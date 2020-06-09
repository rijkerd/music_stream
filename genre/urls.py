from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet

genre_list = GenreViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

genre_detail = GenreViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls
