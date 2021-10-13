import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pages.companies_contact_page import CompaniesAndContactPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestAddCompanyInfo(BaseTest):

    def test_add_company_info(self):
        page = LoginPage(self.driver)
        page2 = CompaniesAndContactPage(self.driver)
        time.sleep(2)
        page.login()
        time.sleep(2)
        page2.fill_up_company_info()
