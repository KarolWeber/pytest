import pdb

import allure
import requests
from src.endpoints.login_page import LoginEndpoints
from src.api.payloads import admin_login_payload
from test_data.credentials import admin_credentials
from utilities.helpers import api_call, HttpMethod


class Admin:
    def __init__(self, username=None, password=None, auto_login=True):
        self.credentials = admin_login_payload.copy()
        if auto_login:
            self.credentials = admin_credentials.copy()
        else:
            self.credentials['username'] = username
            self.credentials['password'] = password
        self.token = None
        self.login_status = None

        self.authenticate()

    @allure.step("Admin login")
    def authenticate(self):
        response = api_call(method=HttpMethod.POST, url=LoginEndpoints.auth, data=self.credentials)
        json_response = response.json()
        token = json_response.get("token")
        if token:
            self.token = token
            self.login_status = "Login successful"
        else:
            self.login_status = json_response.get("reason")
