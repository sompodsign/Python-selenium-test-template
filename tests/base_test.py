import sys
import os.path
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from application_settings.application_settings import ApplicationSettings
from browser_utility.browser import Browser
from pages.page_factory import PageFactory

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):

    browser = Browser()
    application_settings = ApplicationSettings()
    driver = None
    page_factory = None

    def setUp(self):
        # options = Options()
        # options.add_argument("--start-maximized")
        # self.driver.maximize_window()
        # self.driver.set_page_load_timeout(300)
        self.browser.launch_browser()
        self.browser.maximize_browser()
        self.browser.go_to_url(self.application_settings.get_qa_url())
        self.driver = self.browser.get_web_driver()
        self.page_factory = PageFactory(self.driver)

    def tearDown(self):
        self.browser.close_browser()


class TestDemoQaHomepage(BaseTest):

    def test_demo_qa_homepage(self):
        pass
