from datetime import datetime

from backend.session.session_dao import SessionDao

from tests.common import TestMongoDaoBase


class TestSessionDao(TestMongoDaoBase):
    def setUp(self):
        super(TestSessionDao, self).setUp()
        self.session_dao = SessionDao(self.unittest_mongo.core_unittest.session, None)

    def test_create_index(self):
        res = self.session_dao.create_indexes()
        self.assertEqual(res, True)

    def test_update_token(self):
        uid = 1235
        token = 'Test'
        result = self.session_dao.update_user_token(uid, token, datetime)
        self.assertIn(result.modified_count, [1, 0])
        user_token = self.session_dao.get_user_token(uid)
        self.assertEqual(user_token['token'], token)
        self.assertEqual(user_token['user_id'], uid)

    def test_delete_token(self):
        uid = 1235
        token = 'Test'
        result = self.session_dao.update_user_token(uid, token, datetime)
        self.assertIn(result.modified_count, [1, 0])
        delete_result = self.session_dao.delete_user_token(uid)
        self.assertEqual(delete_result.deleted_count, 1)
        user_token = self.session_dao.get_user_token(uid)
        self.assertEqual(user_token, None)
