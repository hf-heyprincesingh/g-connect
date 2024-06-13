from google_workspace_devices.actions.receive_token_action import ReceiveTokenAction
from google_workspace_devices.actions.handle_token_action import HandleTokenAction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class ReceiveTokenView(View):
    def post(self, request, *args, **kwargs):
        action = ReceiveTokenAction()
        return action.handle(request)

class HandleTokenView(View):
    def get(self, request, *args, **kwargs):
        action = HandleTokenAction()
        return action.handle(request)
