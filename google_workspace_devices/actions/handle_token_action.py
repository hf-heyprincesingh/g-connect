from google_workspace_devices.actions.workspace_data_action import WorkspaceDataAction
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import redirect
import logging


logger = logging.getLogger(__name__)

class HandleTokenAction:
    def handle(self, request):
        if request.user.is_authenticated:
            logger.info(f"User {request.user} is authenticated")
            social_account = SocialAccount.objects.filter(user=request.user, provider="google").first()
            if social_account:
                logger.info(f"Found social account: {social_account}")
                social_token = SocialToken.objects.filter(account=social_account).first()
                if social_token:
                    access_token = social_token.token
                    refresh_token = social_token.token_secret
                    logger.info(f"Access Token: {access_token}")
                    logger.info(f"Refresh Token: {refresh_token}")
                    mobile_devices_action = WorkspaceDataAction()
                    mobile_devices_action.execute(access_token=access_token)
                else:
                    logger.warning("No social token found for user")
            else:
                logger.warning("No social account found for user")
        else:
            logger.warning("User is not authenticated")
        return redirect("/")
