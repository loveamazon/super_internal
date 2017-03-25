import unittest

from backend.utils import hash_provider


class TestHashProvider(unittest.TestCase):
    # just for test.
    def test_hash_should_equal_when_same_string(self):
        v1 = "abcdefg"
        hashed = hash_provider.hash_str(v1)
        hashed_2 = hash_provider.hash_str(v1)
        hashed_3 = hash_provider.hash_str("abcdefi")
        self.assertEqual(hashed, hashed_2)
        self.assertNotEqual(hashed_3, hashed_2)
