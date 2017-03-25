from oauth2client import client
from exceptions import GoogleAuthException
from auth_model import AuthResponse
import json
import httplib2


class AuthLogic:
    def __init__(self, redirect_url, client_secret_file_path, client_id_get_url_path, logger):
        self.redirect_url = redirect_url
        self.client_secret_file_path = client_secret_file_path
        self.client_id_get_url_path = client_id_get_url_path
        self.logger = logger
        self.client = client

    def auth(self, auth_request):
        try:
            credentials = self.client.credentials_from_clientsecrets_and_code(self.client_secret_file_path,
                                                                              scope=[
                                                                                  'https://www.googleapis.com/auth/games',
                                                                                  'profile', 'email'],
                                                                              code=auth_request.google_auth_token,
                                                                              redirect_uri=self.redirect_url)
            self.logger.debug('Redirect URI: %s', self.redirect_url)
            self.logger.debug('Returned access_token: %s id_token: %s client id: %s', credentials.access_token,
                              credentials.id_token,
                              credentials.client_id)
            http_auth = credentials.authorize(httplib2.Http())
            resp, content = http_auth.request(self.client_id_get_url_path, method='GET')
            data = json.loads(content)
            self.logger.debug('Req: %s returned: %s w/ content: %s', self.client_id_get_url_path, resp, data)
            ggl_player_id = data['playerId']
            ggl_display_name = data['displayName']
            ggl_title = data['title']
        except Exception, e:
            self.logger.error(
                'Exception occurred during auth flow for {} {}, error message {}'.format(auth_request.google_auth_token,
                                                                                         auth_request.google_player_id,
                                                                                         e.message))
            raise GoogleAuthException(e.message)
        self.logger.debug(
            'Auth token: %s Auth player id: %s Response player id: %s Response player name: %s Response title: %s',
            auth_request.google_auth_token,
            auth_request.google_player_id, ggl_player_id, ggl_display_name, ggl_title)

        return auth_request.google_player_id == ggl_player_id, AuthResponse(ggl_player_id, ggl_display_name,
                                                                            ggl_display_name,
                                                                            ggl_title,
                                                                            None)
