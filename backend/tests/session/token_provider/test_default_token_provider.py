import unittest

from backend.session.token_provider import default_token_provider


class TestDefaultTokenProvider(unittest.TestCase):
    def setUp(self):
        self.token_provider = default_token_provider.DefaultTokenProvider()

    def test_generate_token(self):
        user_id = "4567891"
        token = self.token_provider.generate_token(user_id)
        decode_token, decode_user_id = self.token_provider.decode_token(token)
        self.assertEqual(user_id, decode_user_id)

    def test_xor(self):
        str1 = "abc"
        str2 = "a"
        res = self.token_provider.xor(str1, str2)
        self.assertEqual(res, '\x00\x03\x02')

