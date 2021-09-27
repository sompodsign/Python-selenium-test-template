import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
from pages.login_page_qareceivables import LoginPage2
from pages.new_content_library_page import ContentLib

class testcontentlib(BaseTest):

    def testcontentlibrary(self):
        page1 = LoginPage2(self.driver)
        page1.login()
        time.sleep(5)
        page2 = ContentLib(self.driver)

        page2.click_contentlib_menu()
        time.sleep(5)
        page2.click_sidebar_menu()
        time.sleep(5)
        page2.checkingPinButtonStatus()
        time.sleep(2)
        page2.click_new_folder()
        time.sleep(2)
        page2.fillupdata()
        time.sleep(1)
