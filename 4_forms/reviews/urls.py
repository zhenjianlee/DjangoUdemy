from django.urls import include, path

from .views import ReviewView

urlpatterns=[
    # path('',views.review),
    # path('thank-you',views.thank_you,name='thank-you')
    path('',ReviewView.as_view()),
    path('thank-you',ReviewView.thank_you,name='thank-you')
]