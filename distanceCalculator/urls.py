from django.urls import path
from .views import *

urlpatterns=[
    path('call/', calculate_distance,name='calculate_distance'),
]