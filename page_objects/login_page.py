from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from locators.locators import LoginPageLocators


class LoginPage(BasePage, DriverActions, DriverWaits):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def login(self, email_text, password_text):
        print(email_text, password_text)
        step = 0
        try:
            # step = 1
            # print("Step {} : Checking if email field is present on the page".format(str(step)))
            # assert self.wait_until_visible(10, self.locator.EMAIL_FIELD) is True

            assert self.wait_until_visible(10, self.locator.EMAIL_FIELD) is True
            print("email field is visible")

            print("Typing email address on email field")
            self.type_text(self.locator.EMAIL_FIELD, email_text)

        except Exception as e:
            print(e)
            return False
