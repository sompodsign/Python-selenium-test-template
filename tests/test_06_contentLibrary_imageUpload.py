import sys, os

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time

from tests.base_test import BaseTest
# from pages.ProductPage import ProductPage
from pages.login_page_qareceivables import LoginPage2
from pages.new_content_library_page import ContentLib
from pages.new_content_library_image_upload_page import ContentLibImageUpload as imageuplaod

class testcontentlib(BaseTest):

    def testcontentlibrary(self):
        page1 = LoginPage2(self.driver)
        page1.login()
        time.sleep(15)
        page2 = ContentLib(self.driver)
        page3 = imageuplaod(self.driver)
        page2.click_contentlib_menu()
        time.sleep(15)
        page2.click_sidebar_menu()
        time.sleep(5)
        page2.checkingPinButtonStatus()
        time.sleep(2)
        page3.search_folder()
        time.sleep(2)
        page3.upload_image()
        time.sleep(2)
