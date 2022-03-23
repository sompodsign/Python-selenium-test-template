
from utils.json_utils import load_json


class ApiTestDataProvider:

    login_data = load_json("login_data.json")

    def get_valid_sign_in_data(self):
        return self.login_data["valid_login_data"]

    def get_sign_in_data_without_email(self):
        return self.login_data["no_email_data"]

    def get_sign_in_data_without_password(self):
        return self.login_data["no_password_data"]