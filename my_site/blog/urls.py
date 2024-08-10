from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome , name="welcome"),
    path("/", views.welcome , name = "welcome"),
    path("/posts",views.index , name="index"),
    path("/posts/<str:slug>",views.post, name="post")
]
