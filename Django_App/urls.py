from django.urls import path
from . import views


urlpatterns = [
    path("", views.Welcome, name="Welcome"),
    path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]


