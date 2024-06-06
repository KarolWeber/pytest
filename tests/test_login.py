import pytest
import allure
from src.api.admin import Admin
from test_data import login_test_data
from utilities.tools import assertion


@pytest.mark.login
@allure.suite("Login")
class TestLogin:
    @allure.title("Login successful")
    def test_login_successful(self):
        admin = Admin()
        expected = login_test_data.login_successful["message"]
        current = admin.login_status
        assertion(expected, current)

    @allure.title("Login failed -> Invalid credentials")
    def test_login_successful(self):
        admin = Admin(auto_login=False, username="test", password="test")
        expected = login_test_data.login_failed["message"]
        current = admin.login_status
        assertion(expected, current)

