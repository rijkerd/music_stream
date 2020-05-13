from django.urls import include, path

from src.users import views

urlpatterns = [
    path('', views.UserListView.as_view()),
]
