from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Appliance
from .forms import UserProfileForm, ApplianceForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
import random
from datetime import datetime, timedelta
from .models import Appliance


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                # Attempt to create a new user instance
                user = User.objects.create_user(username=username, email=email, password=password)
                # Redirect to login page
                return redirect('login')
            except IntegrityError:
                # Handle case where username already exists
                form.add_error('username', 'Username is already taken.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # form = UserLoginForm(request.POST)
        # if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            #     login(request, user)
            #     # Redirect to a success page.
            #     return redirect('home')  # Change this to the desired page after login
            # else:
            #     # Return an 'invalid login' error message.
            #     return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
        return redirect('home')  # Change this to the desired page after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_profile(request):
    # Retrieve user profile based on the current user
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_management/user_profile.html', {'user_profile': user_profile})

def edit_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_user_profile.html', {'form': form})

def profiles(request):
    user_profile = UserProfile.objects.filter(user=request.user)

    print(user_profile)

    return render(request, 'profiles.html', {'user_profiles': user_profile})


def add_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            # Create UserProfile
            user_profile = profile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('profiles')
    else:
        appliance_form = ApplianceForm()
        profile_form = UserProfileForm()
    return render(request, 'add_profile.html', {'appliance_form': appliance_form, 'profile_form': profile_form})





def add_appliances_automatic(request):
    user_profile = request.user.userprofile  # Assuming UserProfile is related to User model through OneToOneField
    appliances_data = [
        {"name": "Air conditioner", "type": "AC", "brand": "XYZ", "model_number": "AC123", "serial_number": "SN123456",
         "power_consumption": 1.2},
        {"name": "Water heater", "type": "Heater", "brand": "ABC", "model_number": "WH456", "serial_number": "SN789012",
         "power_consumption": 2},
        {"name": "Electric kettle (5 L)", "type": "Kettle", "brand": "PQR", "model_number": "EK789",
         "serial_number": "SN345678", "power_consumption": random.uniform(2, 2.2)},
        {"name": "Electric Iron", "type": "Iron", "brand": "DEF", "model_number": "EI012", "serial_number": "SN901234",
         "power_consumption": 1.4},
        {"name": "Hair dryer", "type": "Dryer", "brand": "GHI", "model_number": "HD345", "serial_number": "SN567890",
         "power_consumption": 1.2},
        {"name": "Microwave", "type": "Microwave", "brand": "JKL", "model_number": "MM678", "serial_number": "SN123789",
         "power_consumption": random.uniform(1, 1.1)},
        {"name": "Washing machine (5 kg)", "type": "Washer", "brand": "MNO", "model_number": "WM456",
         "serial_number": "SN234567", "power_consumption": 0.85},
        {"name": "Rice cooker", "type": "Cooker", "brand": "RST", "model_number": "RC789", "serial_number": "SN890123",
         "power_consumption": random.uniform(0.7, 0.8)},
        {"name": "Computer", "type": "PC", "brand": "UVW", "model_number": "CP901", "serial_number": "SN234890",
         "power_consumption": 0.75},
        {"name": "Fridge", "type": "Fridge", "brand": "XYZ", "model_number": "FR123", "serial_number": "SN567890",
         "power_consumption": 0.5},
        {"name": "Exhaust hood", "type": "Hood", "brand": "ABC", "model_number": "EH456", "serial_number": "SN123456",
         "power_consumption": 0.212},
        {"name": "Blinder", "type": "Blinder", "brand": "PQR", "model_number": "BL789", "serial_number": "SN678901",
         "power_consumption": 0.205},
        {"name": "Laptop", "type": "Laptop", "brand": "DEF", "model_number": "LT012", "serial_number": "SN345678",
         "power_consumption": 0.1},
        {"name": "Fan (ceiling)", "type": "Fan", "brand": "GHI", "model_number": "FN345", "serial_number": "SN901234",
         "power_consumption": 0.1},
        {"name": "Television", "type": "TV", "brand": "JKL", "model_number": "TV678", "serial_number": "SN123789",
         "power_consumption": 0.08},
        {"name": "Printer", "type": "Printer", "brand": "MNO", "model_number": "PR456", "serial_number": "SN234567",
         "power_consumption": 0.05},
        {"name": "Florescent light", "type": "Light", "brand": "RST", "model_number": "FL789",
         "serial_number": "SN890123", "power_consumption": 0.04},
        {"name": "TM system (receiver + phone + wireless)", "type": "System", "brand": "UVW", "model_number": "TM901",
         "serial_number": "SN234890", "power_consumption": 0.03}
    ]
    start_date = datetime.now() - timedelta(days=365 * 5)  # 5 years ago
    end_date = datetime.now()
    for appliance_data in appliances_data:
        appliance = Appliance.objects.create(
            user=user_profile,
            name=appliance_data['name'],
            type=appliance_data['type'],
            brand=appliance_data['brand'],
            model_number=appliance_data['model_number'],
            serial_number=appliance_data['serial_number'],
            purchase_date=random_date(start_date, end_date),
            warranty_expiry_date=random_date(end_date, end_date + timedelta(days=365 * 5)),
            power_consumption=appliance_data['power_consumption'],
            is_smart_device=random.choice([True, False]),
            measured_power=random.uniform(0, 2),  # Example values, you can adjust as needed
            weekday_energy=random.uniform(0, 10),  # Example values, you can adjust as needed
            weekend_energy=random.uniform(0, 10)  # Example values, you can adjust as needed
        )
        appliance.save()
    return HttpResponse("Appliances added successfully!")


def random_date(start, end):
    """Generate a random date between start and end dates."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def edit_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

def delete_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('profiles')
    return render(request, 'delete_profile.html', {'profile': profile})

def view_appliances(request):
    appliances = Appliance.objects.all()
    return render(request, 'view_appliances.html', {'appliances': appliances})

def add_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appliances')
    else:
        form = ApplianceForm()
    return render(request, 'add_appliance.html', {'form': form})

def edit_appliance(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    if request.method == 'POST':
        form = ApplianceForm(request.POST, instance=appliance)
        if form.is_valid():
            form.save()
            return redirect('appliances')
    else:
        form = ApplianceForm(instance=appliance)
    return render(request, 'edit_appliance.html', {'form': form})

def delete_appliance(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    if request.method == 'POST':
        appliance.delete()
        return redirect('appliances')
    return render(request, 'delete_appliance.html', {'appliance': appliance})

def home(request):
    return render(request, 'home.html')


def room_detail1(request):

    return render(request, 'room1.html')

def room_detail2(request):

    return render(request, 'room2.html')
def room_detail3(request):

    return render(request, 'room3.html')
def room_detail4(request):

    return render(request, 'room4.html')
def room_detail5(request):

    return render(request, 'room5.html')