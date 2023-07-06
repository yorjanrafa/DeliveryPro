from django.urls import path
from django.contrib.auth import views

from .views import home, mapCenter, mapEast, mapWeast

urlpatterns = [
    path('', home, name='home'),
    path('map-east', mapEast, name='map-east'),
    path('map-center', mapCenter, name='map-center'),
    path('map-weast', mapWeast, name='map-weast'),
]
