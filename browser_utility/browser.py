from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from application_settings.application_settings import ApplicationSettings


class Browser:

    web_driver = webdriver
    application_settings = ApplicationSettings()

    def launch_browser(self):
        browser_name = self.application_settings.get_browser_name()
        if browser_name == 'chrome':
            self.web_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == 'firefox':
            self.web_driver = webdriver.Chrome(GeckoDriverManager().install())

    def get_wait(self, wait=10):
        return WebDriverWait(self.web_driver, wait)

    def get_web_driver(self):
        return self.web_driver

    def go_to_url(self, url):
        self.web_driver.get(url)

    def close_browser(self):
        self.web_driver.close()

    def quit_browser(self):
        self.web_driver.quit()

    def maximize_browser(self):
        self.web_driver.maximize_window()

    def accept_alert(self):
        self.web_driver.switch_to.alert.accept()
        self.web_driver.switch_to.default_content()
