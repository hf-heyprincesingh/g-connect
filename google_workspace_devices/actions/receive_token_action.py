from django.http import HttpResponse
from google_workspace_devices.actions.workspace_data_action import WorkspaceDataAction
from google_workspace_devices.utils.parse_data import parse_device_data
import logging
import json

logger = logging.getLogger(__name__)

class ReceiveTokenAction:
    def handle(self, request):
        try:
            body = json.loads(request.body.decode("utf-8"))
            access_token = body.get('access_token')
            handler = WorkspaceDataAction(access_token = access_token)
            handler.execute()
            parse_device_data(access_token = access_token, device_type = "mobiledevices")
            return HttpResponse(status=200)
        except Exception as e:
            logger.error(f"Error processing token: {e}", exc_info=True)
            return HttpResponse(status=500)
