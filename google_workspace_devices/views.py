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

@receiver(social_account_added)
def on_social_account_added(request, sociallogin, **kwargs):
    if sociallogin.is_existing:
        logout(request)
        
        access_token = sociallogin.account.extra_data.get('access_token')
        refresh_token = sociallogin.account.extra_data.get('refresh_token')

        logger.info("Access Token: %s", access_token)
        logger.info("Refresh Token: %s", refresh_token)

        return redirect("/")
        
    else:
        pass
