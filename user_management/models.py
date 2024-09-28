from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    consumer_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)


class Appliance(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    warranty_expiry_date = models.DateField()
    power_consumption = models.DecimalField(max_digits=6, decimal_places=2)  # in watts
    is_smart_device = models.BooleanField(default=False)
    measured_power = models.FloatField()
    weekday_energy = models.FloatField()
    weekend_energy = models.FloatField()

    def __str__(self):
        return self.name







