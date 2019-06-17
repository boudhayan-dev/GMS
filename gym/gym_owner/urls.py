from django.urls import path
from . import views



urlpatterns = [
    path('gym-list', views.gym_list, name='gym_list'),
]