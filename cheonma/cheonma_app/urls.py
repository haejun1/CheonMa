from django.urls import path
from . import views

urlpatterns = [
  path("home/", views.HomeAPIView.as_view(), name="home"),
]