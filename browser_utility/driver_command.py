from selenium import webdriver
from browser_utility.browser import Browser


class DriverCommand:
    webdriver = webdriver

    def driver_command(self):
        browser = Browser("Chrome")
        self.webdriver = browser.webdriver

    def implicitly_wait(self, time):
        self.webdriver.implicitly_wait(time)

    def maximize_windows(self):
        self.webdriver.maximize_window()

    def close_focused_screen(self):
        self.webdriver.close()

    def get_current_page_title(self):
        return self.webdriver.title
    