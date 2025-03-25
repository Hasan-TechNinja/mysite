from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='home'),
    path('update/<int:pk>', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('Tdetails/<int:pk>', views.detailsView, name='Tdetails'),
]
