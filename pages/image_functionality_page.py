import sys, os


# import allure
# from allure_commons.types import AttachmentType

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib
#
from selenium.webdriver.support.select import Select
from pages.welcome_page import WelcomePage
from pages.base_page import BasePage
from pages.new_content_library_image_upload_page import ContentLibImageUpload
import datetime
from utils import ExcelUtils
from utils import locators
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import File_Name_of_the_instance

class contentDownloadImg(BasePage):

    def __init__(self,driver):
        self.locator =locators.contentLibraryImageUpload
        self.imagedownloadlocator = locators.imageDownload
        super(contentDownloadImg, self).__init__(driver)

    def click_on_image(self):
        self.find_element(*self.imagedownloadlocator.clickOnimage).click()

    def imagedownload(self):
        try:
            self.find_element(*self.imagedownloadlocator.clickOnDownloadIcon).click()
            print("clicked on 1st rule")
        except:
            self.click_on_image()
            time.sleep(5)
            self.find_element(*self.imagedownloadlocator.clickOnDownloadIcon2).click()

    def imagedelete(self):
        try:
            self.find_element(*self.imagedownloadlocator.deleteicon).click()
            self.acceptAlertMsg()
            print("clicked on 1st imagedelete")
        except:
            self.click_on_image()
            time.sleep(2)
            element = self.find_element(*self.imagedownloadlocator.deleteicon2)
            element.click()
            time.sleep(2)
            self.acceptAlertMsg()
            print("clicked on 2nd imagedelete")

    def performimagedelete(self):
        self.imagedelete()
        time.sleep(10)
        self.driver.execute_script("window.confirm = function(){return true;}")
