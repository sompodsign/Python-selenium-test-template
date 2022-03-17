import datetime
from utils.ExcelUtils import get_data


class ApplicationSettings:
    file_ext = ""
    browser_name = "chrome"
    url = ""
    image_folder_path = ""
    start_time = datetime.datetime.now()

    # Environment details
    production_url = ""
    dev_url = ""
    qa_url = "https://new-qa.knights.app"
    dev_test_data_file_path = ""
    production_test_data_file_path = ""
    qa_test_data_file_path = "../test_data/qa/dev_test_data.xlsx"
    environment_type = ""

    def setUp(self, os="win", browser="chrome", environment="qa"):
        if os is not None and os.lower() == "win":
            self.file_ext = ".exe"
        else:
            self.file_ext = ""

        self.browser_name = browser

        if environment.lower() == "production":
            self.url = self.production_url
            self.environment_type = "prod"
        elif environment.lower() == "dev":
            self.url = self.dev_url
            self.environment_type = "dev"
        elif environment.lower() == "qa":
            self.url = self.qa_url
            self.environment_type = "qa"

    def get_browser_name(self):
        return self.browser_name

    def get_url(self):
        return self.url

    def get_qa_url(self):
        return self.qa_url

    def get_image_folder_path(self):
        return self.image_folder_path

    def get_start_time(self):
        return self.start_time

    def get_file_ext(self):
        return self.file_ext

    def set_browser_name(self, browser_name):
        self.browser_name = browser_name

    def set_url(self, url):
        self.url = url

    def set_image_folder_path(self, image_folder_path):
        self.image_folder_path = image_folder_path

    def get_test_data_file_path(self, environment):
        if environment == "production":
            return self.production_test_data_file_path
        elif environment == "dev":
            return self.dev_test_data_file_path
        elif environment == "qa":
            return self.qa_test_data_file_path

    def get_test_data(self, environment):
        file_path = self.get_test_data_file_path(environment)
        return get_data(file_path)

    @staticmethod
    def get_login_credentials_table_name():
        return "login"

    @classmethod
    def get_signup_data_table_name(cls):
        return "signup"

    def print_details(self):
        print(self.url, self.environment_type, self.browser_name)
