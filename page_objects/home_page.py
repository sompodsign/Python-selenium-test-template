import allure

from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from locators.locators import HomePageLocators
from utils.logger import CustomLogger

logger = CustomLogger("home_page_test").get_logger()


class HomePage(BasePage, DriverActions, DriverWaits):

    def __init__(self, driver):
        self.home_page_locator = HomePageLocators
        super().__init__(driver)

    @allure.step("Checking the logo is visible properly")
    def check_logo(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.LOGO) is True
            logger.info("Logo is visible on the page")
            return True
        except Exception as e:
            logger.error(f"Logo is not visible on the page: {e}")
            return False

    @allure.step("Checking 'Dogs' menu option is visible")
    def check_dogs_menu(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.DOGS_MENU) is True
            logger.info("Dogs menu is on the top navbar")
            return True
        except Exception as e:
            logger.error(f"Dogs menu is not visible on the page: {e}")
            return False

    @allure.step("Checking 'Races' menu option is visible")
    def check_races_menu(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
            logger.info("'RACES' menu is visible on top navbar")
            return True
        except AssertionError:
            logger.error("'RACES' menu is not visible")
            return False

    @allure.step("Checking 'Marketplace' menu option is on top navbar")
    def check_marketplace_nav(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_MENU) is True
            logger.info("'Marketplace' menu is visible")
            return True
        except AssertionError:
            logger.error("'Marketplace' menu is not visible")
            return False

    @allure.step("Checking 'About' menu option is on top navbar")
    def check_about_nav(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.ABOUT_MENU) is True
            logger.info("'About' menu is visible")
            return True
        except AssertionError:
            logger.error("About menu is not visible")
            return False

    @allure.step("Checking 'Signup' button menu option is on top navbar")
    def check_signup_nav(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.SIGN_UP_BTN) is True
            logger.info("'SIGN UP' button is visible")
            return True
        except AssertionError:
            logger.error("'SIGN UP' button is not visible")
            return False

    @allure.step("Checking 'CONNECT WALLET' button is visible on the top navbar")
    def check_connect_wallet_btn(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.CONNECT_WALLET_BTN) is True
            logger.info("'CONNECT WALLET' button is visible")
            return True
        except AssertionError:
            logger.error("'CONNECT WALLET' button is not visible")
            return False

    @allure.step("Checking 'GET STARTED' button is present on the hero section")
    def check_get_started_btn(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.GET_STARTED_BTN) is True
            logger.info("'GET STARTED' button is visible")
            return True
        except AssertionError:
            logger.error("'GET STARTED' button is not visible")
            return False

    @allure.step("Checking 'Join text: it's time to bet on your fav...' is visible on the page")
    def check_join_text(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.JOIN_TEXT) is True
            logger.info("'Join text: it's time to bet on your fav...' is visible")
            return True
        except AssertionError:
            logger.error("'Join text: it's time to bet on your fav...' is not visible")

    @allure.step("Checking 'Buy Race Courses' section is visible")
    def check_buy_race_text(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.BUY_RACE_COURSES) is True
            logger.info("Buy text section is visible")
            return True
        except AssertionError:
            logger.error("'Buy' text section is not visible")
            return False

    @allure.step("Checking the buttons on Buy courses section")
    def check_buttons_on_buy_courses_section(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.HERO_SECTION_NEXT_BTN) is True
            logger.info("Next button is visible")
            return True
        except AssertionError:
            logger.error("Next button is not visible")
            return False

    @allure.step("Checking 'Join the Champions Club' header on the page")
    def check_champions_club_header(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.CHAMPIONS_HEADER) is True
            logger.info("'Join the Champions Club' header is visible")
            return True
        except AssertionError:
            logger.error("'Join the Champions Club' header is not visible")
            return False

    @allure.step("Checking the 'NFT DOGS CARD' card on the page")
    def check_nft_dogs_card(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.NFT_DOGS_CARD) is True
            assert self.wait_until_visible(self.home_page_locator.EXPLORE_NFT_DOGS_BTN) is True
            logger.info("'NFT DOGS CARD' card is visible")
            return True
        except AssertionError:
            logger.error("'NFT DOGS CARD' card is not visible")
            return False

    @allure.step("Checking the 'Marketplace' card on the page")
    def check_marketplace_card(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_CARD) is True
            assert self.wait_until_visible(self.home_page_locator.ACQUIRE_DOG_BTN) is True
            logger.info("'Marketplace' card is visible")
            return True
        except AssertionError:
            logger.error("'Marketplace' card is not visible")
            return False

    @allure.step("Checking if the 'Race' card is is visible")
    def check_race_card(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
            assert self.wait_until_visible(self.home_page_locator.JOIN_RACES_CARD_BTN) is True
            logger.info("Race card is visible")
            return True
        except AssertionError:
            logger.error("Race card is not on the page")

    @allure.step("Checking if the STORY HEADER: Our Story starts now... is visible")
    def check_story_header(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.STORY_SECTION_HEADER) is True
            logger.info("Story header is visible")
            return True
        except AssertionError:
            logger.error("Story header is not visible")

    @allure.step("Checking if story cards are present on the page")
    def check_story_cards(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.STORY_CARDS) is True
            logger.info("Story cards are visible")
            return True
        except AssertionError:
            logger.error("Story cards are not visible")
            return False

    @allure.step("Checking if the 'Subscribe Now' text is visible")
    def check_subscribe_now_text(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_NOW_TEXT) is True
            logger.info("'Subscribe Now' text is visible")
            return True
        except AssertionError:
            logger.error("'Subscribe Now' text is not visible")
            return False

    @allure.step("Checking if the 'Subscribe Now' button is visible")
    def check_subscribe_now_button(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_BTN) is True
            logger.info("Subscribe Now button is visible")
            return True
        except AssertionError:
            logger.error("Subscribe Now button is not visible")
            return False

    @allure.step("Checking if the Subscribe email input field is visible")
    def check_subscribe_email_input(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_EMAIL_INPUT_FIELD) is True
            logger.info("Subscribe email input is visible")
            return True
        except AssertionError:
            logger.error("Subscribe email input is not visible")
            return False

    @allure.step("Checking if 'Home' as the page title showing in the browser tab")
    def check_home_page_title(self):
        try:
            assert self.check_tab_title("Meta Race") is True
            logger.info("Home page title is correct")
            return True
        except AssertionError:
            logger.error("Home page title is not showing correctly on the browser tab")
            return False

    @allure.step("Checking if the brand logo on footer is visible")
    def check_brand_logo_on_footer(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.FOOTER_LOGO) is True
            assert self.get_attribute_value(self.home_page_locator.FOOTER_LOGO, "xmlns") == "http://www.w3.org/2000/svg"
            logger.info("Brand logo on footer is visible")
            return True
        except AssertionError:
            logger.error("Brand logo on footer is not visible")
            return False

    @allure.step("Checking footer menu items")
    def check_footer_menu_items(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.FOOTER_MENU_ITEMS) is True
            logger.info("Footer menu items are visible")
            return True
        except AssertionError:
            logger.error("Footer menu items are not visible")

    @allure.step("Checking copyright text is showing properly")
    def check_copyright_text(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.COPYRIGHT_TEXT) is True
            assert self.get_element_text(
                self.home_page_locator.COPYRIGHT_TEXT) == "© 2021 SPORTEMON GO. ALL RIGHTS RESERVED."
            logger.info("Copyright text is visible properly")
            return True
        except AssertionError:
            logger.error("Copyright text is not visible")
            return False

    def check_home_page_elements(self):
        """
        This method checks if all the elements on the home page are visible
        :return:
        """
        tests = [
            self.check_logo(),
            self.check_dogs_menu(),
            self.check_races_menu(),
            self.check_marketplace_nav(),
            self.check_about_nav(),
            self.check_signup_nav(),
            self.check_connect_wallet_btn(),
            self.check_get_started_btn(),
            self.check_join_text(),
            self.check_buy_race_text(),
            self.check_buttons_on_buy_courses_section(),
            self.check_champions_club_header(),
            self.check_nft_dogs_card(),
            self.check_marketplace_card(),
            self.check_race_card(),
            self.check_story_header(),
            self.check_story_cards(),
            self.check_subscribe_now_text(),
            self.check_subscribe_now_button(),
            self.check_subscribe_email_input(),
            self.check_home_page_title(),
            self.check_brand_logo_on_footer(),
            self.check_footer_menu_items(),
            self.check_copyright_text(),
        ]
        return all(tests)
