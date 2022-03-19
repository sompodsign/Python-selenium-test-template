import allure
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class LoginPageTest(BaseTest):

    application_settings = ApplicationSettings()

    login_data = application_settings.get_test_data_from_excel(sheet_name="login", table_name="login_data")

    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    def test_01_login_functionality(self):
        login_page = self.page_factory.get_login_page()
        print("Starting to test login functionality")
        login_result = login_page.login(*self.login_data)
        assert login_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_02_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_03_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_04_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_05_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_06_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"

    @allure.title("test_login_functionality_negative")
    @allure.description("Check if login functionalities work properly")
    def test_07_home_functionality(self):
        print("Starting to test Homepage functionality")
        login_page = self.page_factory.get_login_page()
        login_page.login(*self.login_data)
        home_test_result = login_page.test_homepage()
        assert home_test_result is True, "Login failed"
