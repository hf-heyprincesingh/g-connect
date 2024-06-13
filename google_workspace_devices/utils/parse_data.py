import requests
import logging

logger = logging.getLogger(__name__)

class ParseDeviceData:
    def __init__(self, data, device_type):
        self.device_type = device_type
        self.data = data
        
    def parse_mobile_devices(self):
        devices = self.data.get("mobiledevices", [])
        for device in devices:
            name = device.get("name", ["Unknown"])[0]
            device_number = device.get("deviceId", "N/A")
            device_type = device.get("type", "N/A")
            os_version = device.get("os", "N/A")
            model = device.get("model", "N/A")
            email = device.get("email", ["N/A"])[0]
            last_sync = device.get("lastSync", "N/A")
            device_status = device.get("status", "N/A")
            compromised_status = device.get("deviceCompromisedStatus", "N/A")
            print(f"Name: {name}")
            print(f"Device Number: {device_number}")
            print(f"Type: {device_type}")
            print(f"OS Version: {os_version}")
            print(f"Model: {model}")
            print(f"Email: {email}")
            print(f"Last Sync: {last_sync}")
            print(f"Status: {device_status}")
            print(f"Compromised Status: {compromised_status}")
            print("-" * 30)

    def parse_chromeos_devices(self):
        devices = self.data.get("chromeosdevices", [])
        for device in devices:
            annotated_user = device.get("annotatedUser", "Unknown")
            device_id = device.get("deviceId", "N/A")
            serial_number = device.get("serialNumber", "N/A")
            status = device.get("status", "N/A")
            last_sync = device.get("lastSync", "N/A")
            support_end_date = device.get("supportEndDate", "N/A")
            os_version = device.get("osVersion", "N/A")
            platform_version = device.get("platformVersion", "N/A")
            firmware_version = device.get("firmwareVersion", "N/A")
            org_unit_path = device.get("orgUnitPath", "N/A")
            print(f"Annotated User: {annotated_user}")
            print(f"Device ID: {device_id}")
            print(f"Serial Number: {serial_number}")
            print(f"Status: {status}")
            print(f"Last Sync: {last_sync}")
            print(f"Support End Date: {support_end_date}")
            print(f"OS Version: {os_version}")
            print(f"Platform Version: {platform_version}")
            print(f"Firmware Version: {firmware_version}")
            print(f"Org Unit Path: {org_unit_path}")
            print("-" * 30)

    def execute(self):
        if self.device_type == "mobiledevices":
            self.parse_mobile_devices()
        elif self.device_type == "chromeosdevices":
            self.parse_chromeos_devices()
        else:
            logger.error(f"Unsupported device type: {self.device_type}")