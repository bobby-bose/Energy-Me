from django import forms
from .models import UserProfile, Appliance

from django import forms
from django.contrib.auth.models import User

from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 150:
            raise forms.ValidationError("Username must be 150 characters or fewer.")
        return username


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ['address', 'consumer_number', 'phone_number', 'email', 'date_of_birth', 'gender', 'profile_picture']
        labels = {
            'address': 'Address',
            'consumer_number': 'Consumer Number',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'profile_picture': 'Profile Picture'
        }
class ApplianceForm(forms.ModelForm):
    APPLIANCE_TYPES = [
        ('kitchen', 'Kitchen'),
        ('living', 'Living Room'),
        ('personal', 'Personal'),
        ('frontroom', 'Front Room'),
        ('backroom', 'Back Room'),
    ]
    ELECTRICAL_BRANDS = [
        ('Siemens', 'Siemens'),
        ('Philips', 'Philips'),
        ('General Electric (GE)', 'General Electric (GE)'),
        ('Schneider Electric', 'Schneider Electric'),
        ('Honeywell', 'Honeywell'),
        ('Panasonic', 'Panasonic'),
        ('LG Electronics', 'LG Electronics'),
        ('Samsung', 'Samsung'),
        ('Bosch', 'Bosch'),
        ('Hitachi', 'Hitachi'),
    ]

    type = forms.ChoiceField(choices=APPLIANCE_TYPES)
    brand = forms.ChoiceField(choices=ELECTRICAL_BRANDS)  # Assuming a maximum length for brand name
    purchase_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    warranty_expiry_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appliance
        fields = ['name', 'type', 'brand', 'model_number', 'serial_number', 'purchase_date', 'warranty_expiry_date', 'power_consumption', 'is_smart_device']
        labels = {
            'name': 'Name',
            'type': 'Type',
            'brand': 'Brand',
            'model_number': 'Model Number',
            'serial_number': 'Serial Number',
            'purchase_date': 'Purchase Date',
            'warranty_expiry_date': 'Warranty Expiry Date',
            'power_consumption': 'Power Consumption (Watts)',
            'is_smart_device': 'Is Smart Device'
        }
