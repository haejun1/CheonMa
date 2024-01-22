from django.urls import path
from . import views

urlpatterns = [
  path("home/", views.HomeAPIView.as_view(), name="home"),
  path("page/", views.PageAPIView.as_view(), name="page"),
  path("level/", views.LevelAPIView.as_view(), name="level"),
]