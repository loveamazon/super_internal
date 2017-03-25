from backend.account.account_model import AccountInfo


class GoogleAccountDao:
    def __init__(self, google_account_db):
        self.google_account_db = google_account_db

    def create_indexes(self):
        self.google_account_db.create_index("player_id", unique=True)
        self.google_account_db.create_index("user_id", unique=True)
        return True

    def insert_account(self, google_player_id, username, display_name, title, email, user_id):
        user_data = {'player_id': google_player_id, 'name': username, 'title': title, 'email': email,
                     'display_name': display_name, 'user_id': user_id}
        return self.google_account_db.insert(user_data)

    def get_account(self, google_player_id):
        res = self.google_account_db.find_one({'player_id': google_player_id})
        if res is not None:
            user_id = None
            if res['user_id'] is not None:
                user_id = str(res['user_id'])
            return AccountInfo(user_id, res['name'], res['display_name'], res['email'], str(res['player_id']))

        return None

    def delete_account(self, google_player_id):
        return self.google_account_db.delete_many({'player_id': google_player_id})
