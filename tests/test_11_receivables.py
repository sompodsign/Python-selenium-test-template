import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
from pages.login_page_qareceivables import LoginPage2
from pages.add_new_contract_page import addContract

class test_add_new_contact(BaseTest):

    def test_add_contact(self):
        page1 = LoginPage2(self.driver)
        page1.login()
        time.sleep(5)
        page2 = addContract(self.driver)
        page2.add_new_contract()

