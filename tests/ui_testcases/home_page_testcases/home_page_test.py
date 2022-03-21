import allure
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class HomePageTest(BaseTest):
    application_settings = ApplicationSettings()

    @allure.title("Home Page - smoke test")
    @allure.description("Check if homepage elements are visible properly")
    def test_01_home_page_elements_visibility(self):
        home_page = self.page_factory.get_home_page()
        print("Starting to check is homepage functionalities are working properly")
        home_page.check_logo()
        home_page.check_dogs_menu()
        home_page.check_races_menu()
        home_page.check_marketplace_nav()
        home_page.check_about_nav()
        home_page.check_signup_nav()
        home_page.check_connect_wallet_btn()
        home_page.check_get_started_btn()
        home_page.check_join_text()
        home_page.check_buy_race_text()
        home_page.check_buttons_on_buy_courses_section()
        home_page.check_champions_club_header()
        home_page.check_nft_dogs_card()
        home_page.check_marketplace_card()
        home_page.check_race_card()
        home_page.check_story_header()
        home_page.check_story_cards()
        home_page.check_subscribe_now_text()
        home_page.check_subscribe_now_button()
        home_page.check_subscribe_email_input()
