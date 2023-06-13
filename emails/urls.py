from django.urls import path
from emails import views

urlpatterns = [
    path("", views.index),
    path("postuser/", views.postuser),
]