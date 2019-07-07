from django.urls import path
from . import views


urlpatterns = [
    path('gym-list', views.gym_list, name='gym_list'),
    path('dashboard', views.owner_dashboard, name='dashboard'),
    path('login', views.owner_login, name='login'),
    path('logout', views.owner_logout, name='logout'),
    path('registration', views.owner_registration, name='registration'),
    path('my-profile', views.owner_profile, name='my-profile'),
]
