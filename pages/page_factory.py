from page_objects.login_page import LoginPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_login_page(self):
        return LoginPage(self.driver)


