import json
import logging
import unittest

import mock
from backend.login.google.auth_logic import AuthLogic


class TestAuthLogic(unittest.TestCase):
    def setUp(self):
        super(TestAuthLogic, self).setUp()
        self.auth_logic = AuthLogic("", "", "", logging.getLogger())

    def test_auth(self):
        client = mock.Mock()
        self.auth_logic.client = client
        credentials = mock.Mock()
        http_auth = mock.Mock()
        credentials.access_token = "token"
        credentials.id_token = "id_token"
        credentials.client_id = "client_id"
        client.credentials_from_clientsecrets_and_code.return_value = credentials
        credentials.authorize.return_value = http_auth
        http_auth.request.return_value = 1, json.dumps(
            {'playerId': "player_id", "displayName": "displayName", "title": "title"})
        auth_model = mock.Mock()
        auth_model.google_auth_token = "token"
        auth_model.google_player_id = "player_id"
        res, auth_model = self.auth_logic.auth(auth_model)
        self.assertEqual(res, True)
        self.assertEqual(auth_model.display_name, "displayName")
        self.assertEqual(auth_model.external_user_id, "player_id")
