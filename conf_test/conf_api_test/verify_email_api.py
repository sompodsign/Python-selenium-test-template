from conf_test.conf_api_test.base_requests import BaseApi


class VerifyEmailApi(BaseApi):

    def __init__(self, url):
        super().__init__(url)

    def send_otp(self, payload):
        return self.post_request(payload)

    def sign_in_user(self, payload, headers=None):
        return self.post_request(payload, headers)

    def get_user_list(self):
        return self.get_request()

    def get_single_user(self):
        return self.get_request()

    def post_user(self, payload):
        return self.post_request(payload)

    def update_user(self, payload):
        return self.put_request(payload)

    def delete_user(self):
        return self.delete_request()

    def sign_up_with_put(self, payload):
        return self.put_request(payload=payload)
