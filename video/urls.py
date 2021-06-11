"""Video URLS"""

#Django
from django.urls import path

#Views
from video import views

urlpatterns = [
    path("", views.blog , name="blog"),
]
