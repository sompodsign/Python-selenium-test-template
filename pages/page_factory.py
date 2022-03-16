from page_objects.home_page import HomePage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)


