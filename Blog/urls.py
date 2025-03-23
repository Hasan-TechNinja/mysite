from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList, name='blog')
]
