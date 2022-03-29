from utils.email_reader import get_otp_from_email
from utils.json_utils import load_json
from utils.general_functions import get_raw_time
from collections import defaultdict


class ApiTestDataProvider:
    login_data = load_json("login_data.json")
    existing_email = "unidevgo.qa3@gmail.com"
    existing_username = "unidevgo.qa3"
    existing_password = "5946644S"

    def get_valid_sign_in_password(self):
        return self.login_data["valid_login_data"]["password"]

    def get_valid_sign_in_data(self):
        return {"email": self.login_data["valid_login_data"]["email"], "password": self.get_valid_sign_in_password()}

    def get_registered_email(self):
        return self.login_data["valid_login_data"]["email"]

    def get_registered_password(self):
        return self.login_data["valid_login_data"]["password"]

    def get_email_for_otp_send(self):
        return {"email": self.get_existing_email()}

    def get_non_registered_email_object_for_otp_send(self):
        return {"email": self.get_existing_email()}

    @staticmethod
    def get_invalid_email_object_for_otp_send():
        return {"email": "invalid_email"}

    def get_sign_in_data_without_email(self):
        return self.login_data["no_email_data"]

    def get_sign_in_data_without_password(self):
        return self.login_data["no_password_data"]

    @staticmethod
    def get_new_username():
        new_username = "unidev" + get_raw_time()
        return new_username

    @staticmethod
    def get_new_email():
        new_email = "unidev" + get_raw_time() + "@gmail.com"
        return new_email

    @staticmethod
    def get_new_password():
        new_password = "unidev" + get_raw_time()
        return new_password

    @staticmethod
    def get_6_digit_easy_numeric_password():
        return "123456"

    @staticmethod
    def get_6_digit_easy_alphanumeric_password():
        return "abc123"

    @staticmethod
    def get_6_digit_easy_alphanumeric_password_with_special_characters():
        return "abc123!"

    @staticmethod
    def get_6_digit_hard_alpha_num_sym_password():
        return "xfdK45"

    @staticmethod
    def get_8_digit_hard_alpha_num_sym_password():
        return "xfdK45a!"

    @staticmethod
    def get_8_digits_hard_password():
        return "594664a!"

    @staticmethod
    def get_8_digit_easy_password():
        return "12345678"

    @staticmethod
    def get_8_digit_easy_password_with_special_characters():
        return "12345678!"

    @staticmethod
    def get_14_digit_hard_password():
        return "594664a!@#$%^&*"

    def get_existing_username(self):
        return self.existing_username

    def get_existing_email(self):
        return self.existing_email

    def get_existing_email_object(self):
        return {"email": self.existing_email}

    def get_new_valid_register_data(self):
        return {
            "username": self.get_new_username(),
            "email": self.get_new_email(),
            "password": self.get_8_digits_hard_password()
        }

    def get_new_register_data_with_existing_username(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_new_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_new_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_username_and_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_username_and_email_and_password(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_username(self):
        new_admin = defaultdict()
        new_admin["email"] = self.get_new_email()
        new_admin["username"] = ""
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_new_username()
        new_admin["email"] = ""
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_password(self):
        return {
            "username": self.get_new_username(),
            "email": self.get_new_email(),
            "password": ""
        }

    def get_new_register_data_without_username_and_email(self):
        return {
            "username": "",
            "email": "",
            "password": self.get_8_digits_hard_password()
        }

    def get_otp(self):
        return get_otp_from_email({"email": self.get_existing_email(), "password": self.existing_password})

    @staticmethod
    def get_invalid_otp():
        return {"otp": "1234"}

    @staticmethod
    def get_invalid_email():
        return "testemailgamil.com"


a = ApiTestDataProvider()
print(a.get_registered_email())
