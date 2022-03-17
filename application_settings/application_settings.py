import datetime
from utils.ExcelUtils import read_data_from_excel, read_data_from_excel_by_row


class ApplicationSettings:
    """
    This class is used to store the application settings.
    """
    file_ext = ".exe"
    browser_name = "chrome"
    image_folder_path = None
    start_time = datetime.datetime.now()
    configuration_file_path = "../conf_test/configuration.json"

    # Environment details
    environment_type = "qa"
    url = None
    test_data_file_path = "../test_data/{}/test_data.xlsx".format(environment_type)

    def setUp(self, os="win", environment="qa"):

        data_file = "../test_data/{}/test_data.xlsx".format(environment)
        data = read_data_from_excel(data_file, sheet_name="configuration")

        if os is not None and os.lower() == "win":
            self.file_ext = ".exe"
        else:
            self.file_ext = ""

        self.browser_name = data['browser']

        self.environment_type = environment
        self.url = data['base_URL']

    def get_browser_name(self):
        return self.browser_name.lower()

    def get_test_url(self):
        return self.url

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

    def get_test_data_from_excel(self, sheet_name, table_name):
        return read_data_from_excel_by_row(self.test_data_file_path, sheet_name, table_name)

    @staticmethod
    def get_login_credentials_table_name():
        return "login"

    @classmethod
    def get_signup_data_table_name(cls):
        return "signup"

    def get_configuration_file_path(self):
        return self.configuration_file_path

    def print_details(self):
        return self.url, self.browser_name, self.environment_type

