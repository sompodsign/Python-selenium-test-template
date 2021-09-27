import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
from pages.cantact_details_page import AddContactsPage
from pages.login_page import LoginPage

class TestAddContacts(BaseTest):

    def test_add_contacts(self):
            page = LoginPage(self.driver)
            page2 = AddContactsPage(self.driver)
            time.sleep(3)
            page.login()
            time.sleep(2)
            page2.fill_up_add_contacts()
            time.sleep(2)


