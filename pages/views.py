from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('home')

def about(request):
    return HttpResponse('About Us')

def contact(request):
    return HttpResponse('Contact Us')