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
from datetime import datetime
from utils import ExcelUtils
from utils import locators
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import File_Name_of_the_instance


class ContentLib(BasePage):

    def __init__(self, driver):
        self.locator = locators.ContentLib
        super(ContentLib, self).__init__(driver)

    def click_contentlib_menu(self):
        self.find_element(*self.locator.menu_option).click()

    def click_sidebar_menu(self):
        if (self.isDisplayed(*self.locator.sidebarMenu2)):
            pass
        else:
            self.find_element(*self.locator.sidebarMenu).click()

    def click_pin_button(self):
        self.find_element(*self.locator.pinMode).click()

    def checkingPinButtonStatus(self):
        data = self.find_element(*self.locator.sidebarStatus).get_attribute("style")
        if "unpin" in data:
            pass
        else:
            self.click_pin_button()

    def contentlibfunctions(self):
        self.click_contentlib_menu()
        self.click_sidebar_menu()
        self.checkingPinButtonStatus()

    def click_new_folder(self):
        self.find_element(*self.locator.newFolder).click()

    def inputCatName(self, CatalogName):
        self.find_element(*self.locator.catlogName).send_keys(CatalogName)

    def inputDescription(self, Description):
        self.find_element(*self.locator.catDescription).send_keys(Description)

    def inputExpirationDate(self):
        time = str(datetime.now().strftime('%m/%d/%Y'))
        self.find_element(*self.locator.expirationDate).send_keys(time)

    def clickOkbutton(self):
        self.find_element(*self.locator.okButton).click()

    def fillupdata(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForCatalog)

        for r in range(2, row + 1):
            Name = ExcelUtils.readData(clientPath, sheetNameForCatalog, r, 1)
            Description = ExcelUtils.readData(clientPath, sheetNameForCatalog, r, 2)
            time.sleep(1)
            self.inputCatName(Name)
            time.sleep(1)
            self.inputDescription(Description)
            time.sleep(1)
            self.inputExpirationDate()
            time.sleep(1)
            self.clickOkbutton()
            time.sleep(30)
            folderName = self.find_element(*self.locator.folderName).text
            if folderName == Name:
                print("*****************************")
                print("Folder Created")
            else:
                print("*****************************")
                print("Folder not Created")
                print(folderName)
