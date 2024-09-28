from django.urls import path
from . import views

urlpatterns = [
# path('home/', views.home, name='home'),  # Add this line for the home page
    path('profiles/', views.profiles, name='profiles'),
path('profiles/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    path('profiles/<int:profile_id>/delete/', views.delete_profile, name='delete_profile'),
    path('profiles/add/', views.add_profile, name='add_profile'),
    path('add_appliances_automatic/', views.add_appliances_automatic, name='add_appliances_automatic'),
    path('register/', views.register, name='register'),
    path('appliances/', views.view_appliances, name='appliances'),
    path('appliances/add/', views.add_appliance, name='add_appliance'),
    path('appliances/<int:appliance_id>/edit/', views.edit_appliance, name='edit_appliance'),
    path('appliances/<int:appliance_id>/delete/', views.delete_appliance, name='delete_appliance'),

path('room1/', views.room_detail1, name='room1'),
    path('room2/', views.room_detail2, name='room2'),
    path('room3/', views.room_detail3, name='room3'),
    path('room4/', views.room_detail4, name='room4'),
    path('room5/', views.room_detail5, name='room5'),
    path('', views.home, name='home'),
]
