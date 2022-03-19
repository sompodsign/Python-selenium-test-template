import time
import allure

from api_test_data.verify_email.data import email
from api_test_data.otp.data import get_otp, invalid_otp
from api.verify_otp_api import VerifyOtpApi
from api.verify_email_api import VerifyEmailApi
from api_test_data.headers import headers_with_token


# @allure.step("This test verifies that OTP validation works properly")
# def test_successful_otp_verification():
#     otp_api = VerifyOtpApi("/auth/api/verify/otp")
#     verify_email_api = VerifyEmailApi("/auth/api/verify/email")
#     email_result = verify_email_api.send_otp(email)
#     email_response = email_result["status_code"]
#     assert email_response == 201
#     print("\n------Please wait a while until the OTP is sent to your email")
#     time.sleep(40)
#     otp = get_otp()
#     headers_with_token["Authorization"] = "Bearer " + email_result["response"]["data"]
#     otp_response = otp_api.submit_otp(payload={"otp": otp}, headers=headers_with_token)
#     response = otp_response['status_code']
#     assert response == 201


@allure.step("THis test verifies that OTP can't be validated with invalid code")
def test_otp_verification_with_invalid_otp():
    otp_api = VerifyOtpApi("/auth/api/verify/otp")
    otp_response = otp_api.submit_otp(invalid_otp)
    response = otp_response['status_code']
    assert response == 400


@allure.step('Failed verify otp with no token')
def test_026_verify_otp():
    otp_api = VerifyOtpApi("/auth/api/verify/otp")
    result = otp_api.post_request(payload=invalid_otp)
    status_code = result['status_code']
    assert status_code == 400


@allure.step('Failed verify otp with get request')
def test_027_verify_otp():
    otp_api = VerifyOtpApi("/auth/api/verify/otp")
    result = otp_api.get_request(headers=headers_with_token, payload=invalid_otp)
    status_code = result['status_code']
    assert status_code == 400


@allure.step('Failed verify otp with put request')
def test_028_verify_otp():
    otp_api = VerifyOtpApi("/auth/api/verify/otp")
    result = otp_api.put_request(headers=headers_with_token, payload=invalid_otp)
    status_code = result['status_code']
    assert status_code == 400


@allure.step('Failed verify otp with put request')
def test_029_verify_otp():
    otp_api = VerifyOtpApi("/auth/api/verify/otp")
    result = otp_api.delete_request()
    status_code = result['status_code']
    assert status_code == 404
