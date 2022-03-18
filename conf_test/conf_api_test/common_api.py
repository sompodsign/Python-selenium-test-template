import requests
from conf_test.conf_api_test.base_requests import BaseApi


class Api(BaseApi):

    def __init__(self, url):
        super().__init__(url)

    def send(self, payload=None, headers=None):
        return self.post_request(payload, headers)

    def get_request_status(self, payload=None, headers=None):
        return requests.request("GET", self.url, params=payload, headers=headers)

    def patch_request_custom(self, payload=None, headers=None):
        return requests.request("PATCH", self.url, params=payload, headers=headers)