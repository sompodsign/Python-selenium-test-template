import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
# from pages.ProductPage import ProductPage
from pages.login_page_qareceivables import LoginPage2
from pages.add_new_contract_page import addContract


class TestAddNewContact(BaseTest):

    def test_add_new_contact(self):
        page1 = LoginPage2(self.driver)
        page1.login()
        time.sleep(5)
        page2 = addContract(self.driver)
        page2.add_new_contract()
