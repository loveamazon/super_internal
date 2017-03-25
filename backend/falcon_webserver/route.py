import sys

sys.path.append('../../backend')
print sys.path

import falcon
from backend.container import default_container
from falcon_webserver.protobuf import account_login_pb2
from falcon_webserver.protobuf import account_pb2

from backend.login import login_service_error_code
from backend.account import account_error_code
from backend.utils.profile import profile_func
from backend.utils.protocol_handler import handle_get_with_param, handle_post_with_param


class Login:
    @staticmethod
    def response_to_protobuf(proto_response, body):
        mapper = {
            login_service_error_code.OK: account_login_pb2.OK,
            login_service_error_code.AUTH_FAILED: account_login_pb2.AUTH_FAILED,
            login_service_error_code.PASSWORD_INVALID: account_login_pb2.AUTH_FAILED,
            login_service_error_code.USER_NOT_EXIST: account_login_pb2.AUTH_FAILED,
        }

        proto_response.code = mapper[body.code]
        if body.token is not None:
            proto_response.token = body.token

    @profile_func
    @handle_post_with_param(account_login_pb2.AccountLoginRequest, account_login_pb2.AccountLoginResponse,
                            response_to_protobuf)
    def on_post(self, req, resp):
        response = default_container.Services.login_service.login(req.decoded_body)
        resp.body = response


class GoogleLogin:
    @staticmethod
    def response_to_protobuf(proto_response, body):
        mapper = {
            login_service_error_code.OK: account_login_pb2.OK,
            login_service_error_code.AUTH_FAILED: account_login_pb2.AUTH_FAILED
        }

        proto_response.code = mapper[body.code]
        if body.token is not None:
            proto_response.token = body.token

    @profile_func
    @handle_post_with_param(account_login_pb2.AccountLoginRequest, account_login_pb2.AccountLoginResponse,
                            response_to_protobuf)
    def on_post(self, req, resp):
        response = default_container.Services.login_service.login(req.decoded_body)
        resp.body = response


class Account:
    @staticmethod
    def response_to_protobuf(proto_response, body):
        mapper = {
            account_error_code.OK: account_pb2.OK,
            account_error_code.DUPLICATED: account_pb2.DUPLICATED
        }
        proto_response.code = mapper[body['code']]

    @profile_func
    @handle_post_with_param(account_pb2.RegisterAccountRequest, account_pb2.RegisterAccountResponse,
                            response_to_protobuf)
    def on_post(self, req, resp):
        register_request = req.decoded_body
        code, account_info = default_container.Services.account_service.register_account(register_request)
        resp.body = {"code": code, "account_info": account_info}


api = falcon.API()
api.add_route('/login', Login())
api.add_route('/google_login', GoogleLogin())
api.add_route('/account', Account())

# Should in a script and call once.
default_container.create_mongodb_indexes()

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8080, api)
    httpd.serve_forever()
