import allure
from test_data.player_sign_up.data import new_player, new_player_existing_email, \
    new_player_existing_username, \
    new_player_without_username, \
    new_player_without_email, \
    new_player_without_password
from conf_test.conf_api_test.user_api import UserApi
from helpers.general_functions import assert_keys, assert_key_value_pairs


@allure.step('This test verifies that users can sign up as a player.')
def test_successful_player_sign_up():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player)
    response = result["status_code"]
    assert response == 201
    assert_keys("message", "success", "data", response=result["response"])
    assert_key_value_pairs({"message": 'Signed up successfully.', "success": True}, response=result["response"])


@allure.step("This test verifies that user can't sign up as a player with an existing email.")
def test_existing_player_sign_up():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player_existing_email)
    response = result["status_code"]
    assert response == 409


@allure.step("This test verifies that user can't sign up as a player with an existing username.")
def test_existing_player_sign_up():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player_existing_username)
    response = result["status_code"]
    assert response == 409


@allure.step("This test verifies that user can't sign up as a player without username")
def test_player_sign_up_without_username():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player_without_username)
    response = result["status_code"]
    assert response == 400


@allure.step("This test verifies that user can't sign up as a player without email")
def test_player_sign_up_without_email():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player_without_email)
    response = result["status_code"]
    assert response == 400


@allure.step("This test verifies that user can't sign up as a player without password")
def test_player_sign_up_without_password():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_user(new_player_without_password)
    response = result["status_code"]
    assert response == 400


@allure.step("This test verifies that user can't sign up with put request")
def test_player_sign_up_put_request():
    user_api = UserApi("/auth/api/signup")
    result = user_api.sign_up_with_put(new_player)
    response = result["status_code"]
    assert response == 404


@allure.step("This test verifies that user can't sign up with delete request")
def test_player_sign_up_delete_request():
    user_api = UserApi("/auth/api/signup")
    result = user_api.delete_request(new_player)
    response = result["status_code"]
    assert response == 404