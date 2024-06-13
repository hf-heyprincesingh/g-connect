from django.http import HttpResponse
import requests
import logging
import json

logger = logging.getLogger(__name__)


class GoogleTokenHandler:
    def __init__(self, request):
        self.request = request
        self.logger = logging.getLogger(__name__)
        self.credentials_file = "cred.json"
        self.credentials = self.load_credentials()
        self.access_token = self.credentials.get("access_token")
        self.refresh_token = self.credentials.get("refresh_token")
        self.client_id = self.credentials.get("client_id")
        self.client_secret = self.credentials.get("client_secret")

    def load_credentials(self):
        try:
            with open(self.credentials_file, "r") as file:
                return json.load(file)
        except Exception as e:
            self.logger.error(f"Error loading credentials: {e}", exc_info=True)
            return {}

    def save_credentials(self):
        try:
            with open(self.credentials_file, "w") as file:
                json.dump(self.credentials, file, indent=4)
        except Exception as e:
            self.logger.error(f"Error saving credentials: {e}", exc_info=True)

    def is_access_token_valid(self):
        url = "https://www.googleapis.com/oauth2/v1/tokeninfo"
        params = {"access_token": self.access_token}
        response = requests.get(url, params=params)
        return response.status_code == 200

    def refresh_access_token(self):
        url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token",
        }

        self.logger.info(f"Refreshing token with client_id: {self.client_id}")

        response = requests.post(url, data=data)
        if response.status_code == 200:
            new_tokens = response.json()
            self.credentials["access_token"] = new_tokens["access_token"]
            self.credentials["expires_in"] = new_tokens["expires_in"]
            self.credentials["token_type"] = new_tokens["token_type"]
            self.credentials["id_token"] = new_tokens.get(
                "id_token", self.credentials.get("id_token")
            )
            self.save_credentials()
            self.access_token = new_tokens["access_token"]
            return True
        else:
            self.logger.error(f"Error refreshing token: {response.text}", exc_info=True)
            return False

    def handle_token(self):
        if not self.is_access_token_valid():
            self.logger.info("Access token is expired. Refreshing token...")
            if not self.refresh_access_token():
                return HttpResponse(status=500)
            self.logger.info("Token refreshed successfully.")
        else:
            self.logger.info("Access token is valid.")
        self.send_access_token_to_another_app(self.access_token)
        return HttpResponse(status=200)

    def send_access_token_to_another_app(self, access_token):
        url = "http://127.0.0.1:8000/google_workspace_devices/receive_token/"
        headers = {"Content-Type": "application/json"}
        data = {"access_token": access_token}
        response = requests.post(url, headers=headers, json=data)
        return response

    def execute(self):
        return self.handle_token()
