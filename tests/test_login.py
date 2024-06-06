import pytest
import allure
from src.endpoints import login_page
from src.api.admin import Admin


@pytest.mark.login
@allure.suite("Login")
class TestLogin:
    @allure.title("Login successful")
    def test_login_successful(self):
        admin = Admin()
        token = admin.token

        import pdb
        pdb.set_trace()