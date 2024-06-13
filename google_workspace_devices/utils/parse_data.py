def parse_device_data(self, data, device_type):
        devices = data.get(device_type, [])
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