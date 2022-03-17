import allure
import pytest
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings

pytest.mark.usefixtures("setup")


class LoginPageTest(BaseTest):
    application_settings = ApplicationSettings()

    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    def test_login_functionality(self):
        test_data = self.application_settings.get_test_data_from_excel(sheet_name="login", table_name="login_data")

        login_page = self.page_factory.get_login_page()
        print("Starting to test login functionality")
        login_result = login_page.login(*test_data)

        assert login_result is True, "Login failed"
