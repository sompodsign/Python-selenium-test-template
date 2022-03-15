
from selenium.webdriver.support import expected_conditions as EC

from browser_utility.browser import Browser


class DriverWaits:
    """
    This class contains methods to wait for elements to appear on the page.
    """

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def explicit_wait(element, wait_time):
        """
        Wait until element is visible
        :param element:
        :param wait_time:
        :return:
        """
        try:
            Browser.get_wait(wait_time).until(EC.presence_of_element_located(element))
        except Exception as e:
            print(e, "not found")

    @staticmethod
    def wait_until_visible(wait_time, element):
        """
        Wait until element is visible
        :param wait_time:
        :param element:
        :return:
        """
        try:
            Browser.get_wait(wait_time).until(EC.visibility_of_element_located(element));
            return True
        except Exception as e:
            print(e, "not found")
            return False

    @staticmethod
    def wait_till_completely_loaded(wait_time):
        """
        Wait until the page is completely loaded
        :param wait_time:
        :return:
        """
        try:
            js = "return document.readyState"
            Browser.get_wait(wait_time).until(lambda driver: driver.execute_script(js) == "complete")
            return True
        except Exception as e:
            print("Something went wrong: ", e)
            return False

