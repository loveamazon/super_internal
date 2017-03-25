from backend.login import login_service_error_code

from backend.login.login_response_dto import LoginResponseDto


class LoginService:
    def __init__(self, google_auth_logic, session_service, account_service, auth_logic):
        self.google_auth_logic = google_auth_logic
        self.session_service = session_service
        self.account_service = account_service
        self.auth_logic = auth_logic

    def login_google_account(self, request_data):
        auth_result, auth_response = self.google_auth_logic.auth(request_data)
        if auth_result:
            register_account_request = auth_response
            code, account_info = self.account_service.register_google_account(register_account_request)
            token = self.session_service.start_new_session(account_info.user_id)
            user_id = account_info.user_id
            response_code = login_service_error_code.OK
        else:
            response_code = login_service_error_code.AUTH_FAILED

        return LoginResponseDto(response_code, token, user_id)

    def login(self, request_data):
        user_data = self.account_service.get_account_info(request_data)
        token = None
        user_id = None
        if user_data is None:
            response_code = login_service_error_code.USER_NOT_EXIST
            token = None
        else:
            result = self.auth_logic.auth(request_data.password, user_data.password)
            if not result:
                response_code = login_service_error_code.PASSWORD_INVALID
            else:
                user_id = user_data.user_id
                token = self.session_service.start_new_session(user_id)
                response_code = login_service_error_code.OK
        return LoginResponseDto(response_code, token, user_id)
