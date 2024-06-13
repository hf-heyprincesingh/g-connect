from google_token.actions.google_token_handler import GoogleTokenHandler
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class GoogleTokenView(View):
    def get(self, request, *args, **kwargs):
        handler = GoogleTokenHandler(request)
        return handler.execute()
