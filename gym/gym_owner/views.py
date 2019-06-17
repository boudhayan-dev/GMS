from django.shortcuts import render
from .models import Gym
# Create your views here.
def gym_list(request):
    gyms = Gym.objects.all().order_by('created_date')
    print(gyms)
    return render(request, 'gym_owner/gym_list.html', {
        'gyms' : gyms
    })