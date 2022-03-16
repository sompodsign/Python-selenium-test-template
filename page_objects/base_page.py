import sys, os

from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits


class BasePage(DriverActions, DriverWaits):
    """
    Base class to initialize the base page that will be called from all pages
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 30

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source
