from allauth.socialaccount.signals import social_account_added, social_account_updated
from allauth.socialaccount.models import SocialToken
from django.dispatch import receiver

@receiver(social_account_added)
@receiver(social_account_updated)
def social_login_signal(request, sociallogin, **kwargs):
    user = sociallogin.user
    social_account = sociallogin.account
    token = sociallogin.token

    if not user.pk:
        user.save()
        
    if not social_account.pk:
        social_account.user = user
        social_account.save()

    SocialToken.objects.update_or_create(
        account=social_account,
        defaults={'token': token.token, 'token_secret': token.token_secret, 'expires_at': token.expires_at}
    )
