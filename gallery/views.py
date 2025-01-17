from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Photo

image_urls = [
    "https://i.pinimg.com/736x/16/2e/50/162e500f6707f0fcfe64c1cd1ced1405.jpg"
    
    
]

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    # photos = Photo.objects.all()

    return render(request, 'gallery/home.html', {'photos': image_urls})



