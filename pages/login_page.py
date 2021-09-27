import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import time
from pages.base_page import BasePage
from pages.welcome_page import WelcomePage
from utils import ExcelUtils
from utils.locators import *
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import *


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def enter_email(self, username):
        time.sleep(1)
        self.find_element(*self.locator.input_username).send_keys(username)

    def enter_password(self, password):
        time.sleep(1)
        self.find_element(*self.locator.input_password).send_keys(password)

    def click_login_button(self):
        time.sleep(1)
        self.find_element(*self.locator.login_button).click()

    def login(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForLogin)
        for r in range(2, row + 1):
            username = ExcelUtils.readData(clientPath, sheetNameForLogin, r, 1)
            password = ExcelUtils.readData(clientPath, sheetNameForLogin, r, 2)
            time.sleep(1)
            self.enter_email(username)
            time.sleep(1)
            self.enter_password(password)
            time.sleep(1)
            self.click_login_button()
            try:
                self.find_element(*self.locator.escapeLocator).click()

            except:
                pass
            return WelcomePage(self.driver)
