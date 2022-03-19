import time

from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from locators.locators import LoginPageLocators, HomePageLocators


class LoginPage(BasePage, DriverActions, DriverWaits):

    def __init__(self, driver):
        self.login_page_locator = LoginPageLocators
        self.home_page_locator = HomePageLocators
        super().__init__(driver)

    def type_email(self, email):
        print(f"Typing email: {email}")
        self.type_text(self.login_page_locator.EMAIL_FIELD, email)

    def type_password(self, password):
        print(f"Typing password: {password}")
        self.type_text(self.login_page_locator.PASSWORD_FIELD, password)

    def switch_frame(self):
        self.switch_to_frame(self.login_page_locator.CAPTCHA_FRAME)

    def click_check_box(self):
        self.click_on_web_element_with_actions_class(self.login_page_locator.CAPTCHA_CHECK_BOX)

    def click_login_button(self):
        self.click_on_web_element_with_actions_class(self.login_page_locator.LOGIN_BUTTON)

    def login(self, email_text, password_text):

        try:
            step = 0

            self.type_email(email_text)
            step += 1
            print(f"Step {step}: Typed email address on email field")

            self.type_password(password_text)
            step += 1
            print(f"Step {step}: Typed password on password field")

            self.switch_frame()
            step += 1
            print(f"Step {step}: Switched driver to recaptcha iframe")

            self.click_check_box()
            step += 1
            print(f"Step {step}: Clicked on check box")

            self.driver.switch_to.default_content()
            step += 1
            print(f"Step {step}: Switched driver to default content")

            self.wait_till_completely_loaded(30)

            self.click_login_button()
            step += 1
            print(f"Step {step}: Clicked on login button")

            assert self.wait_until_invisibility_of_element(self.login_page_locator.LOGIN_BUTTON) is True
            step += 1
            print(f"Step {step}: Login button is gone")

            return True

        except Exception as e:
            print(e)
            return False

    def test_homepage(self):
        return True if self.wait_until_visible(30, self.home_page_locator.WELCOME_MESSAGE) is True else False
