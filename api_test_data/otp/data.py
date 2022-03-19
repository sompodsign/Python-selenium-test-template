from utils.email_reader import get_otp_from_email

email_credentials = {
    "email": "ss.unidev@gmail.com",
    "password": "5946644S"
}


def get_otp():
    return get_otp_from_email(email_credentials)

invalid_otp = "123456"