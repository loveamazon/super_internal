import uuid


class DefaultTokenProvider:
    def __init__(self):
        pass

    def xor(self, str1, key):
        return ''.join(chr(ord(c) ^ ord(key)) for c in str1)

    def generate_token(self, user_id):
        token = uuid.uuid4().hex
        key = token[:1]
        user_id = self.xor(user_id, key)
        token += user_id.encode("hex")
        return token

    def decode_token(self, token):
        key = token[:1]
        user_id = token[32:].decode("hex")
        user_id = self.xor(user_id, key)
        return uuid, user_id
