import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
# from pages.ProductPage import ProductPage
from pages.login_page_qareceivables import LoginPage2
from pages.new_content_library_page import ContentLib
from pages.image_functionality_page import contentDownloadImg
from pages.new_content_library_image_upload_page import ContentLibImageUpload as imageuplaod


class TestContentnew(BaseTest):

    def testimageDelete(self):
        page1 = LoginPage2(self.driver)
        page1.login()
        time.sleep(5)
        first2 = ContentLib(self.driver)
        first2.click_contentlib_menu()
        time.sleep(5)
        first2.click_sidebar_menu()
        time.sleep(5)
        first2.checkingPinButtonStatus()
        time.sleep(5)
        first3 = imageuplaod(self.driver)
        time.sleep(5)
        first3.search_folder()
        time.sleep(5)
        first4 = contentDownloadImg(self.driver)
        # first4.click_on_image()       #This has been commented due to UI change 05-7-2021
        time.sleep(15)
        first4.performimagedelete()
