import pytest
import allure
from src.api.admin import Admin
from test_data import login_test_data
from utilities.tools import TestResultEvaluator


@pytest.mark.login
@allure.suite("Login")
class TestLogin:
    @allure.title("Login successful")
    def test_login_successful(self):
        """
        Verify admin login functionality.

        Steps:
        1. Authenticate as Admin.
        2. Check login status.
        """
        admin = Admin()
        admin.authenticate()
        expected = login_test_data.login_successful["message"]
        current = admin.login_status
        assertion_list = [
            TestResultEvaluator.compare_results(info="Login status",
                                                expected_result=expected,
                                                current_result=current)
        ]
        assert TestResultEvaluator(assertion_list).result

    @allure.title("Login failed -> Invalid credentials")
    def test_login_invalid_credentials(self):
        """
        Verify admin login failure with incorrect credentials.

        Steps:
        1. Attempt to authenticate with invalid credentials.
        2. Check login status.
        """
        admin = Admin(auto_login=False, username="test", password="test")
        admin.authenticate()
        expected = login_test_data.login_failed["message"]
        current = admin.login_status
        assertion_list = [
            TestResultEvaluator.compare_results(info="Login error message",
                                                expected_result=expected,
                                                current_result=current)
        ]
        assert TestResultEvaluator(assertion_list).result

