import allure
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class HomePageTest(BaseTest):

    application_settings = ApplicationSettings()

    @allure.title("Home Page - smoke test")
    @allure.description("Checking if homepage elements are visible properly")
    def test_01_home_page_elements_visibility(self):
        home_page = self.page_factory.get_home_page()
        print("Starting to check are all homepage elements visible properly")
        assert home_page.check_home_page_elements() is True, "Home page elements are not visible properly"
