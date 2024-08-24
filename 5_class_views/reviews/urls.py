from django.urls import include, path

from . import views

urlpatterns=[
    # path('',views.review),
    path('',views.ReviewView.as_view()),
    path('thank-you',views.thank_you,name='thank-you'),
    path('list',views.ListView.as_view())
]