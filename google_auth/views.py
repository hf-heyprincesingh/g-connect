from django.shortcuts import redirect, render
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def post_login_view(request):
    if request.user.is_authenticated:
        logger.info(f"User {request.user} is authenticated")
        return redirect("google_workspace_devices:handle_token")
    else:
        logger.warning("User is not authenticated")
        return redirect("/")
