from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetchData, name='fetch'),
]
    