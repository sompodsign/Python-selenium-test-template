

import allure

from application_settings.api_application_settings import ApiTestApplicationSettingsProvider
from data_provider.api_test_data_provider import ApiTestDataProvider
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestGamblerSignUp(ApiTestDataProvider):
    gambler_api = ApiTestApplicationSettingsProvider('/auth/api/gambler/signup')

    @allure.step('This test verifies that users can sign up as a gambler.')
    def test_successful_gambler_sign_up(self):
        result = self.gambler_api.post_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 201
            assert result["response"]["message"] == "Signed up successfully."
            assert result["response"]["success"] is True
            logger.info("gambler sign up was successful.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as a player with an existing email.")
    def test_existing_gambler_sign_up(self):
        result = self.gambler_api.post_request(self.get_new_register_data_with_existing_email())
        response = result["status_code"]
        try:
            assert response == 409
            assert result["response"]["message"] == "User already exists"
            assert result["response"]["error"] == "Conflict"
            logger.info("existing gambler sign up was unsuccessful.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as a gambler without username")
    def test_gambler_sign_up_without_username(self):
        result = self.gambler_api.post_request(self.get_new_register_data_without_username())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"][0] == "username should not be empty"
            logger.info("gambler can't sign up without username.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as a player without email")
    def test_gambler_sign_up_without_email(self):
        result = self.gambler_api.post_request(self.get_new_register_data_without_email())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"][0] == "email must be an email"
            logger.info("gambler can't sign up without email.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as a player without password")
    def test_gambler_sign_up_without_password(self):
        result = self.gambler_api.post_request(self.get_new_register_data_without_password())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"] == ['password should not be empty', 'password must be longer than or equal to 6 characters']
            logger.info("gambler can't sign up without password.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up with put request")
    def test_gambler_sign_up_put_request(self):
        result = self.gambler_api.put_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 404
            assert result["response"]["message"] == 'Cannot PUT /auth/api/gambler/signup'
            logger.info("gambler can't sign up with put request.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up with delete request")
    def test_gambler_sign_up_delete_request(self):
        result = self.gambler_api.delete_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 404
            assert result["response"]["message"] == 'Cannot DELETE /auth/api/gambler/signup'
            logger.info("gambler can't sign up with delete request.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False
