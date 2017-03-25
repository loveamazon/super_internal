class AuthRequest:
    def __init__(self, google_player_id, google_auth_token):
        self.google_player_id = google_player_id
        self.google_auth_token = google_auth_token

    def get_auth_token(self):
        return self.google_auth_token

    def get_user_id(self):
        return self.google_player_id


class AuthResponse:
    def __init__(self, google_player_id, name, display_name, title, email):
        self.external_user_id = google_player_id
        self.name = name
        self.display_name = display_name
        self.title = title
        self.email = email
