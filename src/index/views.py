from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from http_path.models import Temp, HumidityURL, PluviometerURL, AnemometerURL

# Create your views here.
# @login_required(login_url='/register')
def index(request):
    return render(request, 'index.html')