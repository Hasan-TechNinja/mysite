from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetchData, name='fetch'),
    path('todo/', views.TodoAPI.as_view(), name='todo'),
    path('todo/<int:pk>', views.TodoAPIDetails.as_view(), name='todo'),
]
    