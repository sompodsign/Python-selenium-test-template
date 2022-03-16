import allure

from tests.base_test import BaseTest


class LoginPageTest(BaseTest):

    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    def test_login_functionality(self):
        login_page = self.page_factory.get_login_page()
        login_result = login_page.login("sompod123@gmail.com", "5946644S")
        assert login_result is True, "Login failed"

