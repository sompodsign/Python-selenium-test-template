import logging

import allure

from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from locators.locators import HomePageLocators
from helper.webdriver_listener import WebDriverListener


class HomePage(BasePage, DriverActions, DriverWaits):

    def __init__(self, driver):
        self.home_page_locator = HomePageLocators
        self.webdriver_listener = WebDriverListener()
        super().__init__(driver)

    @allure.step("Checking the logo is visible properly")
    def check_logo(self):
        print("Step: *****Checking the logo is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.LOGO) is True
        print("Logo is visible on the page")
        return True

    @allure.step("Checking 'Dogs' menu option is visible")
    def check_dogs_menu(self):
        print("Step: *****Checking if the 'Dog' menu is on the page on top nav bar")
        assert self.wait_until_visible(self.home_page_locator.DOGS_MENU) is True
        print("Dogs menu is on the top navbar")

    @allure.step("Checking 'Races' menu option is visible")
    def check_races_menu(self):
        print("Step: *****Checking if the 'Races' menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
        print("RACES menu is visible")

    @allure.step("Checking 'Marketplace' menu option is on top navbar")
    def check_marketplace_nav(self):
        print("Step: *****Checking if marketplace nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_MENU) is True
        print("Marketplace menu is visible")

    @allure.step("Checking 'About' menu option is on top navbar")
    def check_about_nav(self):
        print("Step: *****Checking if about nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.ABOUT_MENU) is True
        print("About menu is visible")

    @allure.step("Checking 'Signup' button menu option is on top navbar")
    def check_signup_nav(self):
        print("Step: *****Checking if signup nav menu option is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.SIGN_UP_BTN) is True
        print("Signup menu is visible")

    @allure.step("Checking 'Connect Wallet' button is visible on the top navbar")
    def check_connect_wallet_btn(self):
        print("Step: *****Checking if connect wallet button is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.CONNECT_WALLET_BTN) is True
        print("Connect wallet button is visible")

    @allure.step("Checking 'Join text: it's time to bet on your fav...' is visible on the page")
    def check_join_text(self):
        print("Step: *****Checking if join text is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.JOIN_TEXT) is True
        print("Join text is visible")

    @allure.step("Checking 'Buy Race Courses' section is visible")
    def check_buy_race_text(self):
        print("Step: *****Checking if buy text section is visible")
        assert self.wait_until_visible(self.home_page_locator.BUY_RACE_COURSES) is True
        print("Buy text section is visible")

    @allure.step("Checking the buttons on Buy courses section")
    def check_buttons_on_buy_courses_section(self):
        print("Step: *****Checking if the buttons on buy courses section are visible")
        assert self.wait_until_visible(self.home_page_locator.HERO_SECTION_NEXT_BTN) is True
        print("Next button is visible")

    @allure.step("Checking the 'Join the Champions Club' header on the page")
    def check_champions_club_header(self):
        print("Step: *****Checking if the 'Join the Champions Club' header is visible")
        assert self.wait_until_visible(self.home_page_locator.CHAMPIONS_HEADER) is True
        print("Champions Club header is visible")

    @allure.step("Checking the 'NFT DOGS CARD' card on the page")
    def check_nft_dogs_card(self):
        print("Step: *****Checking if the 'NFT DOGS CARD' card is visible")
        assert self.wait_until_visible(self.home_page_locator.NFT_DOGS_CARD) is True
        assert self.wait_until_visible(self.home_page_locator.EXPLORE_NFT_DOGS_BTN) is True
        print("NFT DOGS CARD is visible")

    @allure.step("Checking the 'Marketplace' card on the page")
    def check_marketplace_card(self):
        print("Step: *****Checking if the 'Marketplace' card is visible")
        assert self.wait_until_visible(self.home_page_locator.MARKETPLACE_CARD) is True
        assert self.wait_until_visible(self.home_page_locator.ACQUIRE_DOG_BTN) is True
        print("Marketplace card is visible")

    @allure.step("Checking if the 'Race' card is is visible")
    def check_race_card(self):
        print("Step: *****Checking if the 'Race' card is visible on the page")
        assert self.wait_until_visible(self.home_page_locator.RACES_MENU) is True
        assert self.wait_until_visible(self.home_page_locator.JOIN_RACES_CARD_BTN) is True
        print("Race card is visible")

    @allure.step("Checking if the STORY HEADER: Our Story starts now... is visible")
    def check_story_header(self):
        print("Step: ****Checking if the story header is present on the page")
        assert self.wait_until_visible(self.home_page_locator.STORY_SECTION_HEADER) is True
        print("Story header is visible")

    @allure.step("Checking if story cards are present on the page")
    def check_story_cards(self):
        print("Step: ****Checking if the story cards are present on the page")
        assert self.wait_until_visible(self.home_page_locator.STORY_CARDS) is True
        print("Story cards are visible")

    @allure.step("Checking if the 'Subscribe Now' text is visible")
    def check_subscribe_now_text(self):
        print("Step: ****Checking if the 'Subscribe Now' text is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_NOW_TEXT) is True
        print("Subscribe Now text is visible")

    @allure.step("Checking if the 'Subscribe Now' button is visible")
    def check_subscribe_now_button(self):
        print("Step: ****Checking if the 'Subscribe Now' button is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_BTN) is True
        print("Subscribe Now button is visible")

    @allure.step("Checking if the Subscribe email input field is visible")
    def check_subscribe_email_input(self):
        print("Step: ****Checking if the Subscribe email input field is present on the page")
        assert self.wait_until_visible(self.home_page_locator.SUBSCRIBE_EMAIL_INPUT_FIELD) is True
        print("Subscribe email input field is visible")
