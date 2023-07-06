from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request, 'core/base.html')


def mapEast(request):
    return render(request, 'core/maps/east.html')

def mapCenter(request):
    return render(request, 'core/maps/center.html')

def mapWeast(request):
    return render(request, 'core/maps/weast.html')

