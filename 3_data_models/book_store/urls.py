from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("/<slug:slug>", views.book , name="book"),
    # path("/<slug:book_id>", views.book , name="book")
]