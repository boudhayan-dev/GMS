from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from gym_owner.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import Customer
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from gym_owner.forms import AddressForm
# Create your views here.


@login_required(login_url="customer_login")
def customer_dashboard(request):
    user = request.user
    return render(request, 'gym_customer/dashboard.html', {'user': user})


def customer_login(request):
    if request.user.is_authenticated:
        return redirect('customer_dashboard')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'gym_customer/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user.email)
                login(request, user)
                return redirect('customer_dashboard')
            else:
                print('Invalid User ')
        else:
            return render(request, 'gym_customer/login.html', {'form': form})


def customer_logout(request):
    logout(request)
    return redirect('customer_dashboard')


@login_required(login_url='customer_login')
def customer_profile_view(request):
    if request.method == "GET":
        user = request.user
        customer_obj = Customer.objects.get(user=user)
        address_obj = customer_obj.address
        context = {
            'user': user,
            'customer_profile': customer_obj,
            'customer_address': address_obj
        }
        return render(request, 'gym_customer/customer_profile_view.html', context)
        # return render(request, 'gym_customer/base.html', context)

    else:  # else part has to be re-written
        return HttpResponse("INVALID REQUEST")


@login_required(login_url='customer_login')
def customer_profile_edit(request):
    user = request.user
    customer_obj = Customer.objects.get(user=user)
    address_obj = customer_obj.address
    if request.method == 'POST':
        user_form = UserForm(data=request.POST or None, instance=user)
        profile_form = CustomerForm(data=request.POST or None, instance=customer_obj, files=request.FILES)
        address_form = AddressForm(data=request.POST or None, instance=address_obj)
        if user_form.is_valid() and profile_form.is_valid()and address_form.is_valid():
            user_form.save()
            profile_form.save()
            address_form.save()
            return HttpResponseRedirect(reverse('customer_dashboard'))
    else:
        user_form = UserForm(instance=user)
        profile_form = CustomerForm(instance=customer_obj)
        address_form = AddressForm(instance=address_obj)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'address_form': address_form
    }
    return render(request,'gym_customer/customer_profile_edit.html', context)

def menu(request):

    return render(request, 'gym_customer/base.html', {})
