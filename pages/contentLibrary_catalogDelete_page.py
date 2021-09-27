import sys, os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
from selenium.webdriver import ActionChains
class catalogDelete(BasePage):

    def __init__(self,driver):
        self.locator =locators.CatalogDelete
        self.imagedownloadlocator = locators.imageDownload
        super(catalogDelete, self).__init__(driver)

    def RightClickOnCatalog(self):
        source = self.driver.find_element_by_xpath("//a[@data-name='DemoData']")
        action = ActionChains(self.driver)
        action.context_click(source).perform()

    def displayNone(self):
        self.driver.execute_script('document.getElementById("context-menu").style.display="block"')

    def perfomdeletecatalog(self):
        self.driver.find_element_by_xpath("//body[1]/form[1]/div[4]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/ul[1]/li[3]").click()

    def clickonImageoptionTab(self):
        self.driver.find_element_by_xpath("//a[@class='secondaryMenuItem secondaryMenuItemSel']").click()

    def deletecatalog(self):
        try:
            self.RightClickOnCatalog()
        except:
            self.displayNone()
        time.sleep(5)
        self.perfomdeletecatalog()
