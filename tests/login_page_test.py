import allure
from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


# @ddt
class LoginPageTest(BaseTest):
    @allure.title("Login Page - smoke test")
    @allure.description("Check if login functionalities work properly")
    # @data(*ApplicationSettings().get_test_data("qa"))
    # @unpack
    def test_login_functionality(self):
        print(self.application_settings.get_file_ext())

        # login_page = self.page_factory.get_login_page()
        pass
        # print("Starting to test login functionality")
        # login_result = login_page.login("unidevgo.qa1@gmail.com", "5946644Ss@")
        #
        # assert login_result is True, "Login failed"
