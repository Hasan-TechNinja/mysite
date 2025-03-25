from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='home'),
    path('update/', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('details/<int:pk>', views.details, name='details'),
]
