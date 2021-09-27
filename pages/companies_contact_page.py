import sys, os

import allure
from allure_commons.types import AttachmentType

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import CompaniesAndContactPageLocators
from utils.CompanyDataConfigForExcel import *
from pages.welcome_page import WelcomePage
from testconf.testData_configuration_for_run_test import *


class CompaniesAndContactPage(BasePage):
    def __init__(self, driver):
        self.locator = CompaniesAndContactPageLocators
        super(CompaniesAndContactPage, self).__init__(driver)

    def click_add_new_company(self):
        self.find_element(*self.locator.addNewCompanyLocator).click()

    def get_window_handle(self, num):
        return self.driver.window_handles[num]

    def switch_window(self, win):
        return self.driver.switch_to_window(win)

    def enter_company_name(self, companyName):
        self.find_element(*self.locator.CompanyName).send_keys(companyName)

    def add_business_category(self):
        self.find_element(*self.locator.BusinessCategory).click()

    def search_business_category(self, businessCategory):
        self.find_element(*self.locator.SearchBusinessCategory).send_keys(businessCategory)

    def check_business_category(self, businessCategory):
        self.find_element(*self.locator.checkBusinessCategory(businessCategory)).click()

    def done_check_business_category(self):
        self.find_element(*self.locator.BusinessCategoryDone).click()

    def enter_address(self, address):
        self.find_element(*self.locator.AddressField1).send_keys(address)

    def enter_city(self, city):
        self.find_element(*self.locator.cityInput).send_keys(city)

    def enter_zipcode(self, zipcode):
        self.find_element(*self.locator.zipCode).send_keys(zipcode)

    def select_country(self, country):
        select = Select(self.find_element(*self.locator.CountrySelect))
        select.select_by_visible_text(country)

    def validatingCompanyName(self, companyName):
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.find_element(*self.locator.searchCompany).clear()
        time.sleep(1)
        self.find_element(*self.locator.searchCompany).send_keys(companyName)
        time.sleep(1)
        self.find_element(*self.locator.searchGo).click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame("ctl00_MainContent_ifrmCompanyContact")
        time.sleep(2)
        assert self.find_element(*self.locator.assertComapnyName(companyName)).text == companyName
        time.sleep(2)

    def uploadImage(self):
        time.sleep(2)
        self.find_element(*self.locator.editCompany).click()

        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame("ctl00_MainContent_WndHostctrl1_ifrm")

        self.find_element(*self.locator.addCompanyPhoto).click()

        time.sleep(3)
        self.find_element(*self.locator.chooseCompanyPhoto).send_keys(os.getcwd() + "/photos/avatar.jpg")
        self.find_element(*self.locator.uploadcompanyPhoto).click()

    def Click_Save_Button(self):
        self.find_element(*self.locator.saveButton).click()

    def fill_up_company_info(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForCompany)
        for r in range(2, row + 1):
            try:
                companyName = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 1)
                businessCategory = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 2)
                address = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 3)
                city = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 4)
                country = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 5)
                page1 = WelcomePage(self.driver)
                page2 = CompaniesAndContactPage(self.driver)
                print(companyName)
                print("eita row er value{0}".format(row))
                print("eita loop er value {0}".format(r))

                # self.driver.get(ExcelUtils.readData(clientPath, sheetNameForLogin, 2, 3))
                time.sleep(2)
                page1.click_companies_contacts_tab()
                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(5)
                page2.click_add_new_company()

                time.sleep(5)

                self.driver.switch_to.frame(1)

                time.sleep(3)
                self.enter_company_name(companyName)

                time.sleep(1)
                self.add_business_category()

                time.sleep(1)
                self.search_business_category(businessCategory)

                time.sleep(1)
                self.check_business_category(businessCategory)

                time.sleep(1)
                self.done_check_business_category()

                time.sleep(1)
                self.enter_address(address)

                time.sleep(1)
                self.enter_city(city)

                time.sleep(1)
                self.select_country(country)

                time.sleep(1)
                self.Click_Save_Button()

                time.sleep(2)
                self.validatingCompanyName(companyName)
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"{companyName}_screenshot",
                #               attachment_type=AttachmentType.PNG)
                time.sleep(2)
                self.uploadImage()
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"{companyName}_screenshot",
                #               attachment_type=AttachmentType.PNG)

                time.sleep(1)
                self.Click_Save_Button()
                time.sleep(3)
                ExcelUtils.writeData(clientPath, sheetNameForCompany, r, 6, 1)
                time.sleep(3)
            except Exception as e:
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"failed_screenshot",
                #               attachment_type=AttachmentType.PNG)
                # allure.attach(f"Problem Happened, {e}")
                ExcelUtils.writeData(clientPath, sheetNameForCompany, r, 6, 0)
                ExcelUtils.writeData(clientPath, sheetNameForCompany, r, 7, f"Problem Happened, {e}")
                time.sleep(3)
                continue
