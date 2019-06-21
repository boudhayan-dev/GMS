from django.shortcuts import render, redirect
from .models import Gym
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.contrib.auth import login, authenticate, logout

from .forms import OwnerForm, UserForm, AddressForm, LoginForm, GymForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# This view is for TEST purpose only
def gym_list(request):
    gyms = Gym.objects.all().order_by('created_date')
    print(gyms)
    return render(request, 'gym_owner/gym_list.html', {
        'gyms': gyms
    })


@login_required(login_url='login')
def owner_dashboard(request):
    user = request.user
    return render(request, 'gym_owner/dashboard.html', {'user': user})


# Login view for owner
def owner_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'gym_owner/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user.email)
                login(request, user)
                return redirect('dashboard')
            else:
                print('Invalid User ')
        else:
            return render(request, 'gym_owner/login.html', {'form': form})


def owner_logout(request):
    logout(request)
    return redirect('dashboard')


'''
The following view is used to onboard - Gym and the User

Following is the sequence of events -
1. New user visits /owner/registration
2. He fills the form called - "Sign Up - Gym Details" . Self-explanatory
3. He is then re-directed to the same view which now asks for - "Sign Up - Owner Details". Again, self-explanatory.

When the user submits the gym details, his data is not persisted immediately.
Instead, it is stored in session.
Now, the user is redirected to the same view where he is asked to fill in his details.
Once, he enters his details as well, then all the forms/models are persisted.
At this stage, if any error occurs, the entire transaction is rolled-back. This is taken care by @transaction.atomic decorator.
'''


@transaction.atomic
def owner_registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    # If the gym form has been completed
    if ('gymForm' in request.session) and (
            'gymAddressForm' in request.session):

        if request.method == 'GET':
            # Custom UseForm is use
            userForm = UserForm()
            ownerForm = OwnerForm()
            addressForm = AddressForm()
            return render(request,
                          'gym_owner/owner_onboarding.html',
                          {'userForm': userForm,
                           'ownerForm': ownerForm,
                           'addressForm': addressForm,
                           'title': 'Owner Details'})

        if request.method == 'POST':
            # Here 2 address forms are used - 1 for Gym's address and another
            # for the owner
            userForm = UserForm(request.POST)
            ownerForm = OwnerForm(request.POST)  # , prefix = 'owner'
            addressForm = AddressForm(request.POST)

            # Gym form and Gym Address form is already present in session.
            gymForm = GymForm(request.session['gymForm'])
            gymAddressForm = AddressForm(request.session['gymAddressForm'])
            if userForm.is_valid() and ownerForm.is_valid() and addressForm.is_valid():

                # Saving the gym onboarding form
                gymAddress = gymAddressForm.save()
                gymAddress.save()
                gymAddress.refresh_from_db()

                gym = gymForm.save(commit=False)
                gym.address = gymAddress
                gym.save()
                gym.refresh_from_db()

                # Saving the user form

                # Hacky solution
                # Setinng the username field of User model to the email field in ownerForm
                # Seting first_name of User model to first_name of Owner Field
                # Same goes for last name
                # userForm.username = ownerForm.cleaned_data.get('email')
                # This is done bcz the default User model has - blank=True for its name and email field and thus it can be left empty.
                # Somethign which we dont want. Hence, creating these fields on
                # Owner class and manually assigning them to the User model
                # later.
                user = userForm.save()
                user.refresh_from_db()
                user.first_name = ownerForm.cleaned_data.get('first_name')
                user.last_name = ownerForm.cleaned_data.get('last_name')
                user.username = ownerForm.cleaned_data.get('email')
                user.email = ownerForm.cleaned_data.get('email')
                user.set_password(user.password)
                user.save()
                user.refresh_from_db()

                address = addressForm.save()
                address.refresh_from_db()

                print("setting user instance in owner model ")
                ownerForm = ownerForm.save(commit=False)
                ownerForm.gym = gym
                ownerForm.user = user
                ownerForm.address = address
                # ownerForm.full_clean()
                ownerForm.save()
                print("Logging in the user")

                login(request, user)

                # Deleting the Gym Form and the Address Form from the session
                del request.session['gymForm']
                del request.session['gymAddressForm']

                return redirect('dashboard')
            else:
                return render(request,
                              'gym_owner/owner_onboarding.html',
                              {'userForm': userForm,
                               'ownerForm': ownerForm,
                               'addressForm': addressForm,
                               'title': 'Owner Details'})

    else:
        # If the gym details has not been saved in session. then capture that
        # first.
        if request.method == 'GET':
            gymForm = GymForm()
            gymAddressForm = AddressForm()
            return render(request,
                          'gym_owner/gym_onboarding.html',
                          {'gymForm': gymForm,
                           'gymAddressForm': gymAddressForm,
                           'title': 'Gym Details'})

        if request.method == 'POST':
            gymForm = GymForm(request.POST)
            gymAddressForm = AddressForm(request.POST)
            if gymForm.is_valid() and gymAddressForm.is_valid():
                request.session['gymForm'] = gymForm.cleaned_data
                request.session['gymAddressForm'] = gymAddressForm.cleaned_data
                return redirect('signup')
            else:
                return render(request,
                              'gym_owner/gym_onboarding.html',
                              {'gymForm': gymForm,
                               'gymAddressForm': gymAddressForm,
                               'title': 'Gym Details'})
