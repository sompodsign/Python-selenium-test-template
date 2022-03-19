
import allure
from api_test_data.verify_email.data import email, invalid_email, non_registered_email
from api.verify_email_api import VerifyEmailApi


@allure.step('This test verifies that email verification sends OTP to email')
def test_successful_player_sign_up():
    verify_api = VerifyEmailApi("/auth/api/verify/email")
    result = verify_api.send_otp(email)
    response = result["status_code"]
    assert response == 201


@allure.step('This test verifies that OTP does not send to non registered email')
def test_unsuccessful_otp_send_to_non_registered_email():
    verify_api = VerifyEmailApi("/auth/api/verify/email")
    result = verify_api.send_otp(non_registered_email)
    response = result["status_code"]
    assert response == 400


@allure.step('This test verifies that OTP does not send to an invalid email')
def test_unsuccessful_otp_send_to_invalid_email():
    verify_api = VerifyEmailApi("/auth/api/verify/email")
    result = verify_api.send_otp(invalid_email)
    response = result["status_code"]
    assert response == 400
