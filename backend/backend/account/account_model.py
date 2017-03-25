class AccountInfo(object):
    def __init__(self, user_id=None, name=None, display_name=None, email=None, external_user_id=None,
                 hashed_password=None):
        self.user_id = user_id
        self.name = name
        self.display_name = display_name
        self.email = email
        self.external_user_id = external_user_id
        self.password = hashed_password

    def from_json(self, json_dict):
        self.__dict__ = json_dict
