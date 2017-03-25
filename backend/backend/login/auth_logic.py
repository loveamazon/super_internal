class AuthLogic:
    def __init__(self, hash_provider):
        self.hash_provider = hash_provider
        pass

    def auth(self, password, stored_password):
        hashed_password = self.hash_provider.hash_str(password.encode('utf-8'))
        return hashed_password == stored_password
