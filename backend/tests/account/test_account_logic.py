import unittest

import backend.account.account_error_code as account_error_code
import mock
from backend.account.account_logic import AccountLogic
from backend.account.account_model import AccountInfo


class TestAccountLogic(unittest.TestCase):
    def setUp(self):
        super(TestAccountLogic, self).setUp()
        account_dao = mock.Mock()
        google_account_dao = mock.Mock()
        hash_provider = mock.Mock()
        logger = mock.Mock()
        self.account_logic = AccountLogic(account_dao=account_dao, google_account_dao=google_account_dao,
                                          hash_provider=hash_provider, logger=logger)

    def test_register_google_account_duplicated_when_exists(self):
        user_id = "1234"
        name = "test_name"
        display_name = "display_name"
        email = "mail"
        external_id = "4321"
        google_account = AccountInfo(user_id, name, display_name, email, external_id)
        self.account_logic.google_account_dao.get_account.return_value = google_account

        register_account_request = mock.Mock()
        code, result = self.account_logic.register_google_account(register_account_request)
        self.assertEqual(result.name, name)
        self.assertEqual(result.external_user_id, external_id)
        self.assertEqual(result.user_id, user_id)
        self.assertEqual(code, account_error_code.DUPLICATED)

    def test_register_google_account_ok(self):
        user_id = "1234"
        name = "test_name"
        display_name = "display_name"
        email = "mail"
        external_id = "4321"

        self.account_logic.google_account_dao.get_account.return_value = None

        self.account_logic.account_dao.insert_account.return_value = account_error_code.OK, user_id

        self.account_logic.google_account_dao.insert_account.return_value = "uid"

        register_account_request = mock.Mock()
        register_account_request.name = name
        register_account_request.display_name = display_name
        register_account_request.email = email
        register_account_request.external_user_id = external_id

        code, result = self.account_logic.register_google_account(register_account_request)

        self.assertEqual(result.name, name)
        self.assertEqual(result.external_user_id, external_id)
        self.assertEqual(result.user_id, user_id)
        self.assertEqual(code, account_error_code.OK)
