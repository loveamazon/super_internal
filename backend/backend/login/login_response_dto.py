class LoginResponseDto(object):
    def __init__(self, code, token, user_id):
        self.code = code
        self.token = token
        self.user_id = user_id
