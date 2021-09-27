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
from utils import locators
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import *


class AddContactsPage(BasePage):
    unique_id = 0
    def __init__(self, driver):
        self.locator = locators.ContactsLocator
        self.locator_for_company = locators.CompaniesAndContactPageLocators
        super(AddContactsPage, self).__init__(driver)

    def search_for_company(self, companyName):
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.find_element(*self.locator_for_company.searchCompany).clear()
        time.sleep(1)
        self.find_element(*self.locator_for_company.searchCompany).send_keys(companyName)
        time.sleep(1)
        self.find_element(*self.locator_for_company.searchGo).click()


    def click_add_new_contacts(self):
        self.find_element(*self.locator.addContactsLocator).click()

    
    def select_situation(self, situation):
        select = Select(self.find_element(*self.locator.situation))
        select.select_by_visible_text(situation)

    def add_firstName(self, firstName):
        self.find_element(*self.locator.firstName).send_keys(firstName)

    def add_lastname(self, lastName):
        self.find_element(*self.locator.LastName).send_keys(lastName)

    def add_email(self, email):
        self.find_element(*self.locator.email).send_keys(email)

    
    def add_role(self):
        self.find_element(*self.locator.addRoles).click()

    def search_role(self, role):
        self.find_element(*self.locator.searchRole).send_keys(role)

    def check_role(self, role):
        self.find_element(*self.locator.checkRoles(role)).click()

    def check_role_done(self):
        self.find_element(*self.locator.checkRoleDone).click()

    def Click_Save_Button(self):
        self.find_element(*self.locator.saveBtn3).click()

    def uploadImage(self, contactName):
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame("ctl00_MainContent_ifrmCompanyContact")
        time.sleep(2)
        self.find_element(*self.locator.editContacts(contactName)).click()

        time.sleep(5)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame("ctl00_MainContent_WndHostctrl1_ifrm")
        time.sleep(5)
        self.find_element(*self.locator.addPhoto).click()

        time.sleep(3)
        self.find_element(*self.locator.fileUpload).send_keys(os.getcwd()+"/photos/avatar.jpg")
        self.find_element(*self.locator.buttonUplaod).click()

    def click_systemUser(self):
        self.find_element(*self.locator.systemUser).click()

    def click_internalUser(self):
        self.find_element(*self.locator.internalUser).click()

    def click_externalUser(self):
        self.find_element(*self.locator.externalUser).click()

    
    def fill_up_add_contacts(self):

        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForContact)
        for r in range(2, row + 1):
            try:
                companyName = ExcelUtils.readData(clientPath, sheetNameForContact, r, 7)
                situation = ExcelUtils.readData(clientPath, sheetNameForContact, r, 1)
                firstName = ExcelUtils.readData(clientPath, sheetNameForContact, r, 2)
                lastName = ExcelUtils.readData(clientPath, sheetNameForContact, r, 3)
                email = ExcelUtils.readData(clientPath, sheetNameForContact, r, 4)
                role = ExcelUtils.readData(clientPath, sheetNameForContact, r, 5)
                SysUser = ExcelUtils.readData(clientPath, sheetNameForContact, r, 6)
                contactName = str(firstName )+ " " + str(lastName)

                page1 = WelcomePage(self.driver)
                time.sleep(3)
                self.driver.get(ExcelUtils.readData(clientPath, sheetNameForLogin, 2, 3))
                time.sleep(2)

                page1.click_companies_contacts_tab()

                self.driver.switch_to_default_content()
                time.sleep(2)
                self.search_for_company(companyName)

                self.driver.switch_to_default_content()
                time.sleep(2)
                self.driver.switch_to.frame("ctl00_MainContent_ifrmCompanyContact")

                time.sleep(2)
                self.click_add_new_contacts()

                time.sleep(5)
                self.driver.switch_to_default_content()
                self.driver.switch_to.frame("ctl00_MainContent_WndHostctrl1_ifrm")

                time.sleep(1)
                self.select_situation(situation)

                time.sleep(1)
                self.add_firstName(firstName)

                time.sleep(1)
                self.add_lastname(lastName)

                time.sleep(1)
                self.add_email(email)

                time.sleep(1)
                self.add_role()

                time.sleep(1)
                self.search_role(role)

                time.sleep(1)
                self.check_role(role)

                time.sleep(1)
                self.check_role_done()

                time.sleep(1)
                self.click_systemUser()

                if SysUser == "Internal":
                    time.sleep(1)
                    self.click_internalUser()
                elif SysUser == "External":
                    time.sleep(1)
                    self.click_externalUser()


                time.sleep(1)
                self.Click_Save_Button()
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"{lastName}saved_screenshot",
                #               attachment_type=AttachmentType.PNG)
                time.sleep(1)

                self.uploadImage(contactName)

                # allure.attach(self.driver.get_screenshot_as_png(), name=f"{lastName}_screenshot", attachment_type=AttachmentType.PNG)

                time.sleep(1)
                self.Click_Save_Button()

                time.sleep(3)
                ExcelUtils.writeData(clientPath, sheetNameForContact, r, 9, 1)
                time.sleep(3)
            except Exception as e:

                # allure.attach(self.driver.get_screenshot_as_png(), name=f"failed_screenshot",
                #               attachment_type=AttachmentType.PNG)
                # allure.attach(f"Problem Happened, {e}")
                ExcelUtils.writeData(clientPath, sheetNameForContact, r, 9, 0)
                time.sleep(3)
                continue
