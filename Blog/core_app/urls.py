
from .views import *
from django.urls import path

urlpatterns = [
    path('', render_home, name= 'home'),
    path('registration/', render_registration, name= 'registration'),
    path('authorization/', render_authorization, name= 'authorization')
]