class SessionDao:
    def __init__(self, session_db, logger):
        self.logger = logger
        self.session_db = session_db

    def create_indexes(self):
        self.session_db.create_index("create_date", expireAfterSeconds=7200)
        self.session_db.create_index("token")
        return True

    def update_user_token(self, user_id, token, time_provider):
        return self.session_db.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "token": token,
                    "user_id": user_id
                },
                "$currentDate": {
                    "create_date": True
                },
            },
            upsert=True,
        )
    #                    "create_date": time_provider.utcnow(),

    def delete_user_token(self, user_id):
        return self.session_db.delete_one({"user_id": user_id})

    def get_user_token(self, user_id, token=None):
        if token is not None:
            return self.session_db.find_one({"user_id": user_id, "token": token})
        else:
            return self.session_db.find_one({"user_id": user_id})
