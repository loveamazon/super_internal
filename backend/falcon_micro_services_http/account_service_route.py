import json
from wsgiref import simple_server
import sys

sys.path.append('../../backend')

import falcon
from backend.container.micro_service import account_service_container
from falcon_webserver.protobuf import account_pb2

from backend.account import account_error_code
from backend.utils.profile import profile_func
from backend.utils.protocol_handler import handle_get_with_param, handle_post_with_param


class Account:
    @staticmethod
    def get_account_response_to_protobuf(proto_response, body):
        proto_response.user_id = body.user_id
        proto_response.name = body.name
        proto_response.email = body.email
        proto_response.display_name = body.display_name
        proto_response.password = body.password
        proto_response.external_user_id = body.proto_response

    @profile_func
    @handle_get_with_param(account_pb2.GetAccountResponse, get_account_response_to_protobuf)
    def on_get(self, req, resp):
        account_info = account_service_container.Services.account_service.get_account_info(req.decoded_body)
        resp.body = account_info

    @staticmethod
    def register_response_to_protobuf(proto_response, body):
        mapper = {
            account_error_code.OK: account_pb2.OK,
            account_error_code.DUPLICATED: account_pb2.DUPLICATED
        }
        proto_response.code = mapper[body['code']]

    @profile_func
    @handle_post_with_param(account_pb2.RegisterAccountRequest,
                            account_pb2.RegisterAccountResponse,
                            register_response_to_protobuf)
    def on_post(self, req, resp):
        register_request = req.decoded_body
        code, account_info = account_service_container.Services.account_service.register_account(register_request)
        resp.body = {"code": code, "account_info": account_info}


api = falcon.API()
api.add_route('/account', Account())

# Should in a script and call once.
account_service_container.create_mongodb_indexes()

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8088, api)
    httpd.serve_forever()
