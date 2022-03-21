import allure
# from loguru import logger

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
        except Exception as e:
            logger.error(f"Logo is not visible on the page: {e}")

    @allure.step("Checking 'Dogs' menu option is visible")
    def check_dogs_menu(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.DOGS_MENU) is True
            logger.info("Dogs menu is on the top navbar")
        except Exception as e:
            logger.error(f"Dogs menu is not visible on the page: {e}")

    @allure.step("Checking 'Races' menu option is visible")
    def check_races_menu(self):
        # logger.info("Step: *****Checking if the 'Races' menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
        logger.info("RACES menu is visible")

    @allure.step("Checking 'Marketplace' menu option is on top navbar")
    def check_marketplace_nav(self):
        # logger.info("Step: *****Checking if marketplace nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_MENU) is True
        logger.info("Marketplace menu is visible")

    @allure.step("Checking 'About' menu option is on top navbar")
    def check_about_nav(self):
        # logger.info("Step: *****Checking if about nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.ABOUT_MENU) is True
        logger.info("About menu is visible")

    @allure.step("Checking 'Signup' button menu option is on top navbar")
    def check_signup_nav(self):
        # logger.info("Step: *****Checking if signup nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.SIGN_UP_BTN) is True
        logger.info("Signup menu is visible")

    @allure.step("Checking 'Connect Wallet' button is visible on the top navbar")
    def check_connect_wallet_btn(self):
        # logger.info("Step: *****Checking if connect wallet button is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.CONNECT_WALLET_BTN) is True
        logger.info("Connect wallet button is visible")

    @allure.step("Checking 'GET STARTED' button is present on the hero section")
    def check_get_started_btn(self):
        # logger.info("Step: *****Checking if 'GET STARTED' button is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.GET_STARTED_BTN) is True
        logger.info("GET STARTED button is visible")

    @allure.step("Checking 'Join text: it's time to bet on your fav...' is visible on the page")
    def check_join_text(self):
        # logger.info("Step: *****Checking if join text is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.JOIN_TEXT) is True
        logger.info("Join text is visible")

    @allure.step("Checking 'Buy Race Courses' section is visible")
    def check_buy_race_text(self):
        # logger.info("Step: *****Checking if buy text section is visible")
        assert self.wait_until_visible(self.home_page_locator.BUY_RACE_COURSES) is True
        logger.info("Buy text section is visible")

    @allure.step("Checking the buttons on Buy courses section")
    def check_buttons_on_buy_courses_section(self):
        # logger.info("Step: *****Checking if the buttons on buy courses section are visible")
        assert self.wait_until_visible(self.home_page_locator.HERO_SECTION_NEXT_BTN) is True
        logger.info("Next button is visible")

    @allure.step("Checking the 'Join the Champions Club' header on the page")
    def check_champions_club_header(self):
        # logger.info("Step: *****Checking if the 'Join the Champions Club' header is visible")
        assert self.wait_until_visible(self.home_page_locator.CHAMPIONS_HEADER) is True
        logger.info("Champions Club header is visible")

    @allure.step("Checking the 'NFT DOGS CARD' card on the page")
    def check_nft_dogs_card(self):
        # logger.info("Step: *****Checking if the 'NFT DOGS CARD' card is visible")
        assert self.wait_until_visible(self.home_page_locator.NFT_DOGS_CARD) is True
        assert self.wait_until_visible(self.home_page_locator.EXPLORE_NFT_DOGS_BTN) is True
        logger.info("NFT DOGS CARD is visible")

    @allure.step("Checking the 'Marketplace' card on the page")
    def check_marketplace_card(self):
        # logger.info("Step: *****Checking if the 'Marketplace' card is visible")
        assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_CARD) is True
        assert self.wait_until_visible(self.home_page_locator.ACQUIRE_DOG_BTN) is True
        logger.info("Marketplace card is visible")

    @allure.step("Checking if the 'Race' card is is visible")
    def check_race_card(self):
        # logger.info("Step: *****Checking if the 'Race' card is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
        assert self.wait_until_visible(self.home_page_locator.JOIN_RACES_CARD_BTN) is True
        logger.info("Race card is visible")

    @allure.step("Checking if the STORY HEADER: Our Story starts now... is visible")
    def check_story_header(self):
        # logger.info("Step: ****Checking if the story header is present on the page")
        assert self.wait_until_visible(self.home_page_locator.STORY_SECTION_HEADER) is True
        logger.info("Story header is visible")

    @allure.step("Checking if story cards are present on the page")
    def check_story_cards(self):
        # logger.info("Step: ****Checking if the story cards are present on the page")
        assert self.wait_until_visible(self.home_page_locator.STORY_CARDS) is True
        logger.info("Story cards are visible")

    @allure.step("Checking if the 'Subscribe Now' text is visible")
    def check_subscribe_now_text(self):
        # logger.info("Step: ****Checking if the 'Subscribe Now' text is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_NOW_TEXT) is True
        logger.info("Subscribe Now text is visible")

    @allure.step("Checking if the 'Subscribe Now' button is visible")
    def check_subscribe_now_button(self):
        # logger.info("Step: ****Checking if the 'Subscribe Now' button is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_BTN) is True
        logger.info("Subscribe Now button is visible")

    @allure.step("Checking if the Subscribe email input field is visible")
    def check_subscribe_email_input(self):
        # logger.info("Step: ****Checking if the Subscribe email input field is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_EMAIL_INPUT_FIELD) is True
        logger.info("Subscribe email input field is visible")
