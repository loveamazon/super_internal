from backend.account.external.google.google_account_dao import GoogleAccountDao

from tests.common import TestMongoDaoBase


class TestGoogleAccountDao(TestMongoDaoBase):
    def setUp(self):
        super(TestGoogleAccountDao, self).setUp()
        self.google_account_dao = GoogleAccountDao(self.unittest_mongo.core_unittest.google_account)
        res = self.google_account_dao.create_indexes()
        self.assertEqual(res, True)

    def test_insert_google_account_ok(self):
        google_player_id = "12121"
        name = "test_name_1"
        title = "title_test"
        display_name = "display_name_test"
        email = "email_test@cc.com"
        user_id = "uid_test"
        new_id = self.google_account_dao.insert_account(google_player_id, name, display_name, title, email,
                                                        user_id)
        self.assertNotEqual(new_id, None)
        user_info = self.google_account_dao.get_account(google_player_id)
        self.assertEqual(user_info.name, name)
        self.assertEqual(user_info.email, email)
        self.assertEqual(user_info.external_user_id, google_player_id)
        self.google_account_dao.delete_account(google_player_id)
