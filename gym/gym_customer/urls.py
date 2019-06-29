from django.urls import path
from .views import *


urlpatterns = [
    # path('dashboard', customer_dashboard, name='customer_dashboard'),
    path('login', customer_login, name='customer_login'),
    path('logout', customer_logout, name='customer_logout'),
    path('view-profile', customer_profile_view, name='profile_view'),
    path('edit-profile', customer_profile_edit, name='profile_edit'),
    path('menu', menu, name='customer_dashboard'),

]
