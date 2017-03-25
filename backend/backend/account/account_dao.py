import pymongo
from bson.objectid import ObjectId

import account_error_code
from account_model import AccountInfo


class AccountDao:
    def __init__(self, account_db, logger):
        self.account_db = account_db
        self.logger = logger

    def create_indexes(self):
        self.account_db.create_index("name", unique=True)
        return True

    def insert_account(self, name, password_hashed, display_name, email):
        user_data = {'name': name, 'password': password_hashed, 'email': email,
                     'display_name': display_name}
        try:
            user_id = self.account_db.insert(user_data)
        except pymongo.errors.DuplicateKeyError, e:
            self.logger.error("Duplicated item found, error message %s, name %s", e.message, name)
            return account_error_code.DUPLICATED, None

        return account_error_code.OK, str(user_id)

    def get_account_by_name(self, name):
        res = self.account_db.find_one({'name': name})
        if res is not None:
            return AccountInfo(str(res['_id']), res['name'], res['display_name'], res['email'], None, res['password'])

        return None

    def get_account(self, user_id):
        res = self.account_db.find_one({'_id': ObjectId(user_id)})
        if res is not None:
            return AccountInfo(str(res['_id']), res['name'], res['display_name'], res['email'], None)

        return None

    def delete_account(self, user_id):
        return self.account_db.delete_many({'_id': ObjectId(user_id)})
