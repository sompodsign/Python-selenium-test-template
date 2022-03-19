import allure
import pytest
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class LoginPageTest(BaseTest):

    application_settings = ApplicationSettings()

    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    def test_01_login_functionality(self):
        login_data = self.application_settings.get_test_data_from_excel(sheet_name="login", table_name="login_data")
        login_page = self.page_factory.get_login_page()
        print("Starting to test login functionality")
        login_result = login_page.login(*login_data)
        assert login_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_02_home_functionality(self):
        login_page = self.page_factory.get_login_page()
        print("Starting to test login functionality")
        login_result = login_page.test_homepage()
        assert login_result is True, "Login failed"
