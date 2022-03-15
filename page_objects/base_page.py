import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self, driver, base_url=""):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_all_element(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            var = EC.visibility_of_all_elements_located
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def get_text(self, locator):
        return self.driver.locator.text

    def sendkeys(self, path, value):
        self.driver.find_element(path).send_keys(value)

    def right_click(self, locator):
        element = self.find_element(locator)
        right_click = ActionChains(self.driver).move_to_element(element)
        right_click.context_click().perform()

    def accept_alert_msg(self):
        obj = self.driver.switch_to.alert
        obj.accept()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def javascript_alert_accept(self):
        self.driver.execute_script("window.confirm = function(){return true;}")

    def is_displayed(self, *locator):
        return self.driver.find_element(*locator).is_displayed()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, data, *locator):
        self.driver.find_element(*locator).send_keys(data)

    def change_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def change_to_default_frame(self):
        self.driver.switch_to.default_content()

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.visibility_of_element_located(*locator))
        return element
