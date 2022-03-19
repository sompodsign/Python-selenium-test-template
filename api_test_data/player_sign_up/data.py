from utils.general_functions import get_raw_time


new_player = {
    "username": "unidevgoplayer{}".format(get_raw_time()),
    "email": "unidevgotest.qa1{}@gmail.com".format(get_raw_time()),
    "password": "12345678S",
}

new_player_existing_email = {
    "username": "unidev{}".format(get_raw_time()),
    "email": "unidevgo.qa202207151918@gmail.com",
    "password": "12345678S"
}

new_player_existing_username = {
    "username": "unidev202207152310",
    "email": "unidevgo.qa{}@gmail.com".format(get_raw_time()),
    "password": "12345678S",
}

new_player_without_username = {
    "username": "",
    "email": "unidevgo.qa{}@gmail.com".format(get_raw_time()),
    "password": "12345678S",
}

new_player_without_email = {
    "username": "unidev202207152310",
    "password": "12345678S",
}

new_player_without_password = {
    "username": "unidev202207152310",
    "email": "unidevgo.qa{}@gmail.com".format(get_raw_time()),
    "password": "",
}