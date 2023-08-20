from .views import login, get_code, fill_profile_data, profile
from django.urls import path

urlpatterns = [
    path('', profile, name='profile'),
    path('login/', login, name='login'),
    path('login/code', get_code, name='login_code'),
    path('login/profile', fill_profile_data, name='fill_profile')
]
