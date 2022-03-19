from api.user_api import UserApi
from test_data.user_data.data import valid_user_data


def get_user_id():
    """
    Returns the current user id
    """
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(valid_user_data)
    user_id = result['response']['id']
    return user_id


current_user_id = get_user_id()
