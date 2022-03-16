from tests.base_test import BaseTest


class TestDemoPage(BaseTest):

    def test_home_page(self):

        home_page = self.page_factory.get_home_page()
        title = home_page.get_page_title()
        assert title == "ToolsQA"

