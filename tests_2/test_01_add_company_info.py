import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from pages.login_page_qareceivables import LoginPage2
from pages.companies_contact_page import CompaniesAndContactPage
from tests.base_test import BaseTest


class TestAddCompanyInfo(BaseTest):

    def test_add_company_info(self):
        page = LoginPage2(self.driver)
        page2 = CompaniesAndContactPage(self.driver)
        time.sleep(2)
        page.login()
        time.sleep(2)
        page2.fill_up_company_info()
