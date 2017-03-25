import unittest

import pymongo

from tests import config


class TestMongoDaoBase(unittest.TestCase):
    def setUp(self):
        self.unittest_mongo = pymongo.MongoClient(config.MONGODB_URI)
