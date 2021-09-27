import sys, os

# import allure
# from allure_commons.types import AttachmentType

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select
from pages.welcome_page import WelcomePage
from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import IPandProductsPageLocators
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import *


class IPandProductsPage(BasePage):
    def __init__(self, driver):
        self.locator = IPandProductsPageLocators
        super(IPandProductsPage, self).__init__(driver)

    def click_add_new_ip(self):
        self.find_element(*self.locator.addNewIP).click()

    def add_licensor(self):
        self.find_element(*self.locator.addLicensor).click()

    def search_licensor(self, licensor):
        self.find_element(*self.locator.searchLicensor).send_keys(licensor)

    def check_licensor(self, licensor):
        self.find_element(*self.locator.checklicensors(licensor)).click()

    def done_check_licensor(self):
        self.find_element(*self.locator.LicensorCheckDone).click()

    def enter_intel_prop(self, intel):
        self.find_element(*self.locator.intellectualProperty).send_keys(intel)

    def enter_primary_id(self, id):
        self.find_element(*self.locator.primaryID).send_keys(id)

    def enter_owner(self, owner):
        self.find_element(*self.locator.owner).send_keys(owner)



    def add_ip_type(self):
        self.find_element(*self.locator.addIPType).click()

    def search_ip_type(self, ipType):
        self.find_element(*self.locator.searchIPType).send_keys(ipType)

    def check_ip_type(self, ipType):
        self.find_element(*self.locator.checkIpType(ipType)).click()

    def done_check_ip_type(self):
        self.find_element(*self.locator.checkIPTypeDone).click()





    def select_language(self, language):
        select = Select(self.find_element(*self.locator.Language))
        select.select_by_visible_text(language)

    def uploadImage(self):
        time.sleep(2)
        self.find_element(*self.locator.addIpPhoto).click()

        time.sleep(3)
        self.find_element(*self.locator.chooseIpPhoto).send_keys(os.getcwd()+"/photos/avatar.jpg")
        self.find_element(*self.locator.uplaodIpPhoto).click()


    def Click_Save_Button(self):
        self.find_element(*self.locator.saveButton2).click()

    def click_cancel_btn(self):
        self.find_element(*self.locator.cancelButton2).click()


    def fill_up_add_ip(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForIP)
        for r in range(2, row + 1):
            try:
                licensor = ExcelUtils.readData(clientPath, sheetNameForIP, r, 1)
                intel = ExcelUtils.readData(clientPath, sheetNameForIP, r, 2)
                primaryId = ExcelUtils.readData(clientPath, sheetNameForIP, r, 3)
                owner = ExcelUtils.readData(clientPath, sheetNameForIP, r, 4)
                lang = ExcelUtils.readData(clientPath, sheetNameForIP, r, 5)
                ipType = ExcelUtils.readData(clientPath, sheetNameForIP, r, 6)
                page1 = WelcomePage(self.driver)
                page2 = IPandProductsPage(self.driver)
                self.driver.get(ExcelUtils.readData(clientPath, sheetNameForLogin, 2, 3))
                time.sleep(2)
                page1.click_ip_and_Products_tab()
                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(2)
                page2.click_add_new_ip()

                time.sleep(5)
                self.driver.switch_to.frame(0)

                time.sleep(1)
                self.add_licensor()

                time.sleep(1)
                self.search_licensor(licensor)

                time.sleep(1)
                self.check_licensor(licensor)

                time.sleep(1)
                self.done_check_licensor()

                time.sleep(1)
                self.enter_intel_prop(intel)

                time.sleep(1)
                self.enter_primary_id(primaryId)

                time.sleep(1)
                self.enter_owner(owner)

                time.sleep(1)
                self.add_ip_type()

                time.sleep(1)
                self.search_ip_type(ipType)

                time.sleep(1)
                self.check_ip_type(ipType)

                time.sleep(1)
                self.done_check_ip_type()

                time.sleep(1)
                self.select_language(lang)

                time.sleep(1)
                self.Click_Save_Button()

                time.sleep(2)
                self.uploadImage()

                # allure.attach(self.driver.get_screenshot_as_png(), name=f"{intel}_screenshot", attachment_type=AttachmentType.PNG)

                time.sleep(2)
                self.Click_Save_Button()


                time.sleep(3)
                self.click_cancel_btn()
                time.sleep(3)
                ExcelUtils.writeData(clientPath, sheetNameForIP, r, 7, 1)
                time.sleep(3)
            except Exception as e:
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"failed_screenshot",
                #               attachment_type=AttachmentType.PNG)
                # allure.attach(f"Problem Happened, {e}")
                ExcelUtils.writeData(clientPath, sheetNameForIP, r, 7, 0)
                time.sleep(3)
                continue