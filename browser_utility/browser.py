from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from application_settings.application_settings import ApplicationSettings
from utils.json_utils import json_reader


class Browser:

    web_driver = webdriver
    application_settings = ApplicationSettings()
    data = json_reader(application_settings.get_configuration_file_path())

    environment = data['settings']['environmentType']

    def launch_browser(self):
        """
        This method will launch the browser based on the environment type
        :return:
        """
        self.application_settings.setUp(environment=self.environment)
        browser_name = self.application_settings.get_browser_name()
        if browser_name == 'chrome':
            self.web_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == 'firefox':
            self.web_driver = webdriver.Firefox(GeckoDriverManager().install())
        elif browser_name == 'ie':
            self.web_driver = webdriver.Ie(IEDriverManager().install())
        elif browser_name == 'edge':
            self.web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser_name == 'opera':
            self.web_driver = webdriver.Opera(OperaDriverManager().install())

    def get_wait(self):
        return WebDriverWait(self.web_driver, 30)

    def get_web_driver(self):
        return self.web_driver

    def go_to_url(self):
        self.web_driver.get(self.application_settings.get_test_url())

    def close_browser(self):
        self.web_driver.close()

    def quit_browser(self):
        self.web_driver.quit()

    def maximize_browser(self):
        self.web_driver.maximize_window()

    def accept_alert(self):
        self.web_driver.switch_to.alert.accept()
        self.web_driver.switch_to.default_content()
