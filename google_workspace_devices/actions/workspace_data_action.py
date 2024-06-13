from google_workspace_devices.utils.parse_data import ParseDeviceData
from google_workspace_devices.constants import URL
import requests
import logging

logger = logging.getLogger(__name__)


class WorkspaceDataAction:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_mobile_devices(self):
        url = URL["GOOGLE_WORKSPACE_MOBILE_DEVICES"]
        headers = { 
            "Authorization": f"Bearer {self.access_token}",
            "Content-length": "0",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            handler = ParseDeviceData(data=data, device_type="mobiledevices")
            handler.execute()
        else:
            logger.error(
                f"Failed to retrieve data: {response.status_code} - {response.text}"
            )

    def get_chromeos_devices(self):
        url = URL["GOOGLE_WORKSPACE_CHROMEOS_DEVICES"]
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-length": "0",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            handler = ParseDeviceData(data=data, device_type="chromeosdevices")
            handler.execute()
        else:
            logger.error(
                f"Failed to retrieve data: {response.status_code} - {response.text}"
            )

    def execute(self):
        self.get_mobile_devices()
