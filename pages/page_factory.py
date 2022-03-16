from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from page_objects.login_page import LoginPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_driver_actions_object(self):
        return DriverActions(self.driver)

    def get_driver_waits_object(self):
        return DriverWaits(self.driver)


