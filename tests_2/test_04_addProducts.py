import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
from pages.ProductPage import ProductPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage


class TestAddProducts(BaseTest):

    def test_add_products(self):
            page = LoginPage(self.driver)
            page1 = WelcomePage(self.driver)
            page2 = ProductPage(self.driver)
            time.sleep(2)
            page.login()
            time.sleep(2)
            page2.fill_up_add_product()
            time.sleep(2)
