from django.shortcuts import redirect, render
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount, SocialToken
import logging
from allauth.socialaccount.signals import pre_social_login, social_account_added, social_account_updated
from django.dispatch import receiver

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect("/")

def post_login_view(request):
    if request.user.is_authenticated:
        logger.info(f"User {request.user} is authenticated")
        social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
        if social_account:
            logger.info(f"Found social account: {social_account}")
            social_token = SocialToken.objects.filter(account=social_account).first()
            if social_token:
                access_token = social_token.token
                refresh_token = social_token.token_secret
                logger.info(f"Access Token: {access_token}")
                logger.info(f"Refresh Token: {refresh_token}")
                print(f"Access Token: {access_token}")
                print(f"Refresh Token: {refresh_token}")
            else:
                logger.warning("No social token found for user")
        else:
            logger.warning("No social account found for user")
    else:
        logger.warning("User is not authenticated")
    
    return redirect("/") 



@receiver(social_account_added)
@receiver(social_account_updated)
@receiver(pre_social_login)
def social_login_signal(sender, request, sociallogin, **kwargs):
    if sociallogin.token: 
        token = sociallogin.token
        SocialToken.objects.update_or_create(
            account=sociallogin.account,
            defaults={'token': token.token, 'token_secret': token.token_secret}
        )