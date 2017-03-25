import urllib3
from urllib3.connection import HTTPConnection

from backend.account import AccountInfo
import json


class AccountServiceRemote:
    def __init__(self, account_service_remote_base_url):
        self.account_service_remote_base_url = account_service_remote_base_url
        self.http = urllib3.PoolManager(num_pools=10, socket_options=HTTPConnection.default_socket_options)

    def get_account_info(self, request):
        url = self.account_service_remote_base_url + "account"
        response = self.http.request('GET', url, headers={"Content-Type": "application/json", "Keep-Alive": "True"},
                                     fields={"name": request.name})

        info = AccountInfo()
        info.from_json(json.loads(response.data.decode('utf-8')))
        return info

    def register_account(self, register_account_request):
        pass
        # url = self.account_service_remote_base_url + "/account"
        # return requests.post(url, register_account_request)

    def register_google_account(self, register_account_request):
        pass
        # url = self.account_service_remote_base_url + "/google_account"
        # return requests.post(url, register_account_request)
