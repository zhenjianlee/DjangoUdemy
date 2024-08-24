from django.urls import include, path

from . import views

urlpatterns=[
    # path('',views.review),
    path('',views.ReviewView.as_view()),
    path('form',views.ReviewFormView.as_view()),
    path('create',views.ReviewCreateView.as_view()),
    path('thank-you',views.thank_you,name='thank-you'),
    path('listnormal',views.NormalListView.as_view()),
    path('listview',views.ListView.as_view()),
    path('template/<int:id>',views.ReviewTemplateView.as_view()),
    path('detail/<int:pk>',views.ReviewDetailView.as_view()),
]