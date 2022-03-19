
from api.base_requests import BaseApi


class VerifyApi(BaseApi):

    def __init__(self, url):
        super().__init__(url)

    def send_otp(self, payload, headers=None):
        return self.post_request(payload, headers)

    def send(self, payload, headers=None):
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

