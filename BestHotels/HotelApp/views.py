from django.shortcuts import render
from django.http import request

from django.http.response import Http404

# Create your views here.
def About_Page(request):
    return render(request, 'About.html')

def Contact_Page(request):
    return render(request, 'Contact.html')

def News_Page(request):
    return render(request, 'News.html')

def Home_Page(request):
    
    return render(request, 'Home.html')
def Rooms_Page(request):
    return render(request, 'Rooms.html')