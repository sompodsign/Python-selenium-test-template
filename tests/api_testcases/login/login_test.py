import allure
from api.user_api import UserApi
from api_test_data.login_data.data import valid_login_credentials, \
    no_email_data, no_password_data

user_api = UserApi('/auth/api/login')


@allure.step('Successful user login with valid data test')
def test_valid_signin():
    result = user_api.sign_in_user(payload=valid_login_credentials)
    status_code = result['status_code']
    print(result)
    assert status_code == 201


@allure.step('Fail sign in without username')
def test_sign_in_without_email():
    result = user_api.sign_in_user(payload=no_email_data)
    status_code = result['status_code']
    assert status_code == 400


@allure.step('Fail sign in without password')
def test_sign_in_without_password():
    result = user_api.sign_in_user(payload=no_password_data)
    status_code = result['status_code']
    assert status_code == 400


@allure.step('Fail sign in get request')
def test_invalid_sign_in_get_request():
    result = user_api.get_request(payload=no_password_data)
    status_code = result['status_code']
    assert status_code == 404


@allure.step('Fail sign in put request')
def test_invalid_sign_in_put_request():
    result = user_api.put_request(payload=no_password_data)
    status_code = result['status_code']
    assert status_code == 404


@allure.step('Fail sign in delete')
def test_invalid_sign_in_delete_request():
    result = user_api.delete_request()
    status_code = result['status_code']
    assert status_code == 404
