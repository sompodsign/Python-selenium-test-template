import sys
import os.path
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(300)

    def tearDown(self):
        self.driver.close()
