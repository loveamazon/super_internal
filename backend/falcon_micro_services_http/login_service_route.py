from wsgiref import simple_server
import sys

sys.path.append('../../backend')
import falcon
from backend.container.micro_service import login_service_container
from falcon_webserver.protobuf import account_login_pb2
from backend.login import login_service_error_code
from backend.utils.profile import profile_func
from backend.utils.protocol_handler import handle_post_with_param


class Login:
    @staticmethod
    def response_to_protobuf(self, proto_response, body):
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
        response = login_service_container.Services.login_service.login(req.decoded_body)
        resp.body = response


api = falcon.API()
api.add_route('/login', Login())

# Should in a script and call once.
login_service_container.create_mongodb_indexes()

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8089, api)
    httpd.serve_forever()
