
from tests.base_test import BaseTest


class LoginPageTest(BaseTest):

    def validate_login_functionality(self):
        home_page = self.page_factory.get_login_page()
        title = home_page.get_page_title()
        assert title == "ToolsQA"

