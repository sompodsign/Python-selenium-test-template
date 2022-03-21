from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from page_objects.home_page import HomePage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def get_driver_actions_object(self):
        return DriverActions(self.driver)

    def get_driver_waits_object(self):
        return DriverWaits(self.driver)


