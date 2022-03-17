import allure
from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


@ddt
class LoginPageTest(BaseTest):

    application_settings = ApplicationSettings()

    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    @data(*["sompoe123@gmail.com", "sompoe123"])
    @unpack
    def test_login_functionality(self, email, password):
        print(email, password)
        login_page = self.page_factory.get_login_page()
        print("Starting to test login functionality")
        login_result = login_page.login(email, password)

        assert login_result is True, "Login failed"
