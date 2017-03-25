import logging

from backend.account import account_error_code
from backend.account.account_dao import AccountDao

from tests.common import TestMongoDaoBase


class TestAccountDao(TestMongoDaoBase):
    def setUp(self):
        super(TestAccountDao, self).setUp()
        logger = logging.getLogger()
        self.account_dao = AccountDao(self.unittest_mongo.core_unittest.account, logger)
        res = self.account_dao.create_indexes()
        self.assertEqual(res, True)

    def test_insert_account_ok(self):
        name = "test_name_1"
        password = "password_test"
        display_name = "display_name_test"
        email = "email_test@cc.com"
        result, uid = self.account_dao.insert_account(name, password, display_name, email)
        self.assertNotEqual(uid, None)
        user_info = self.account_dao.get_account(uid)
        self.assertEqual(user_info.name, name)
        self.assertEqual(user_info.email, email)
        self.assertEqual(user_info.user_id, uid)
        self.account_dao.delete_account(uid)

    def test_delete_account_ok(self):
        name = "test_name_2"
        password = "password_test"
        display_name = "display_name_test"
        email = "email_test@cc.com"
        result, uid = self.account_dao.insert_account(name, password, display_name, email)
        self.assertNotEqual(uid, None)
        delete_result = self.account_dao.delete_account(uid)
        self.assertEqual(delete_result.deleted_count, 1)
        user = self.account_dao.get_account_by_name(name)
        self.assertEqual(user, None)

    def test_insert_fail_when_dup(self):
        name = "test_name_3"
        password = "password_test"
        display_name = "display_name_test"
        email = "email_test@cc.com"
        result, uid = self.account_dao.insert_account(name, password, display_name, email)
        self.assertNotEqual(uid, None)
        current_uid = uid
        result, uid = self.account_dao.insert_account(name, password, display_name, email)
        self.assertEqual(uid, None)
        self.assertEqual(result, account_error_code.DUPLICATED)
        self.account_dao.delete_account(current_uid)
