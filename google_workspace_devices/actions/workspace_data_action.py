from google_workspace_devices.utils.parse_data import parse_device_data
import requests
import logging

logger = logging.getLogger(__name__)


class WorkspaceDataAction:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_mobile_devices(self):
        url = "https://admin.googleapis.com/admin/directory/v1/customer/my_customer/devices/mobile"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-length": "0",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            parse_device_data(data=data, device_type="mobiledevices")
        else:
            logger.error(
                f"Failed to retrieve data: {response.status_code} - {response.text}"
            )

    def get_chromeos_devices(self):
        url = "https://admin.googleapis.com/admin/directory/v1/customer/my_customer/devices/chromeos"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-length": "0",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            parse_device_data(data=data, device_type="chromeosdevices")
        else:
            logger.error(
                f"Failed to retrieve data: {response.status_code} - {response.text}"
            )

    def execute(self):
        self.get_mobile_devices()
