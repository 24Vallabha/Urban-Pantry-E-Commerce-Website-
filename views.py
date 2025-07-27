from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def electronic_view(request):
    return render(request, 'products/electronic.html')

def decorative_view(request):
    return render(request, 'products/decorative.html')

def fruits_view(request):
    return render(request, 'products/fruits.html')

def clothing_view(request):
    return render(request, 'products/clothing.html')

def pet_view(request):
    return render(request, 'products/pet.html')
# Create your views here.
# own/views.py
def television_view(request):
    return render(request, 'products/television.html')

def mixers_view(request):
    return render(request, 'products/mixers.html')

def phones_view(request):
    return render(request, 'products/phones.html')

def washing_view(request):
    return render(request, 'products/washing.html')

def watch_view(request):
    return render(request, 'products/watch.html')

def air_view(request):
    return render(request, 'products/air.html')

def speaker_view(request):
    return render(request, 'products/speaker.html')

def chimney_view(request):
    return render(request, 'products/chimney.html')

def cart_view(request):
    return render(request, 'cart.html')

def buy_view(request):
    return render(request, 'buy.html')

def about_view(request):
    return render(request,'about.html')

def write_view(request):
    return render(request,'write.html')

def services_view(request):
    return render(request,'services.html')

def contact_view(request):
    return render(request,'contact.html')