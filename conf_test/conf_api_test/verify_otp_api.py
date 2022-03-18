from conf_test.conf_api_test.base_requests import BaseApi


class VerifyOtpApi(BaseApi):

    def __init__(self, url):
        super().__init__(url)

    def submit_otp(self, payload=None, headers=None):
        return self.post_request(payload=payload, headers=headers)

