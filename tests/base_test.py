import sys
import os.path
import unittest
from browser_utility.browser import Browser
from pages.page_factory import PageFactory

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):
    browser = Browser()
    driver = None
    page_factory = None

    def setUp(self):
        self.browser.launch_browser()
        self.browser.go_to_url()
        self.browser.maximize_browser()
        self.driver = self.browser.get_web_driver()
        self.page_factory = PageFactory(self.driver)

    def tearDown(self):
        self.browser.close_browser()

