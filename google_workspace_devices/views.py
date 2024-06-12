from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect("/")

