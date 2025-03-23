from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList, name='blog'),
    path('details/<int:pk>', views.BlogDetails, name='details'),
]
