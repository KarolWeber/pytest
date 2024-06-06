import allure
from src.api.endpoints import Endpoints
from utilities.payload_creator import PayloadCreator
from src.api.booking import Booking
from utilities.credentials import admin_credentials
from utilities.helpers import api_call, HttpMethod


class Admin:
    def __init__(self, username=None, password=None, auto_login=True):
        self.credentials = PayloadCreator.Login.admin_login_payload(username, password)
        if auto_login:
            self.credentials = admin_credentials.copy()
        else:
            self.credentials['username'] = username
            self.credentials['password'] = password
        self.token = None
        self.login_status = None

        self.authenticate()
        self.booking = Booking(self)

    @allure.step("Admin login")
    def authenticate(self):
        """
        Admin login
        :return:
        """
        response = api_call(method=HttpMethod.POST, url=Endpoints.login, data=self.credentials)
        if response.status_code == 200:
            json_response = response.json()
            token = json_response.get("token")
            if token:
                self.token = token
                self.login_status = "Login successful"
            else:
                self.login_status = json_response.get("reason")
        else:
            self.login_status = response

