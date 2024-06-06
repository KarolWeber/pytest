import requests
from src.endpoints.login_page import LoginEndpoints
from utilities.helpers import api_call, HttpMethod
from test_data.credentials import admin_credentials


class Admin:
    def __init__(self, username=None, password=None):
        self.credentials = admin_credentials
        if username is not None:
            self.credentials["username"] = username
        if password is not None:
            self.credentials["password"] = password
        self.token = None
        self.login_error = None
        self.authenticate()

    def authenticate(self):
        response = api_call(method=HttpMethod.GET, url=LoginEndpoints.auth, data=self.credentials)
        json_response = response.json()
        token = json_response.get("token")
        if token:
            self.token = token
        else:
            self.login_error = json_response.get("reason")
