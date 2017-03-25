class SessionService:
    def __init__(self, session_dao, token_provider, time_provider, logger):
        self.session_dao = session_dao
        self.time_provider = time_provider
        self.token_provider = token_provider
        self.logger = logger

    def start_new_session(self, user_id):
        self.logger.debug("Start to refresh token for user %s", user_id)
        new_token = self.token_provider.generate_token(user_id)
        self.session_dao.update_user_token(user_id, new_token, self.time_provider)
        self.logger.debug("Refresh token %s for user %s", new_token, user_id)
        return new_token
