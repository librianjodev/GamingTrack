from django.shortcuts import render
from .forms import registerUserForm
from django.http import HttpResponse

# Create your views here.

def registerUser(response):
    form = registerUserForm()
    return render(response, "user/register.html", {"form":form})
