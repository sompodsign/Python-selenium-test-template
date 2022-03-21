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
        print("Checking the logo is visible on the page")
        assert self.wait_until_visible(30, self.home_page_locator.LOGO) is True
        print("Logo is visible on the page")
        return True
