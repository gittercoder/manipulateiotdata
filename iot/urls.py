from django.urls import path
from . import views

urlpatterns = [
    path('insert-sensor/', views.sensor_insert, name='sensor_insert'),
    path('insert-user/', views.user_insert, name='user_insert'),
]