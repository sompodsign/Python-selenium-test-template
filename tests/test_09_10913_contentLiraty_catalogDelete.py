import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from tests.base_test import BaseTest
# from pages.ProductPage import ProductPage
from pages.login_page_qareceivables import LoginPage2
from pages.new_content_library_page import ContentLib
from pages.image_functionality_page import contentDownloadImg
from pages.new_content_library_image_upload_page import ContentLibImageUpload as imageuplaod
from pages.contentLibrary_catalogDelete_page import catalogDelete

class TestCatalogDelete(BaseTest):
    def testcatalogdelete(self):
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
        page3 = imageuplaod(self.driver)
        page3.search_folder()
        time.sleep(10)
        page4 = catalogDelete(self.driver)
        page4.deletecatalog()
        time.sleep(5)
        page4.clickonImageoptionTab()
        page3.search_folder()
        time.sleep(5)