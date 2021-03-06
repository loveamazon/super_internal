import logging

import backend.utils.hash_provider as hash_provider
import dependency_injector.containers as containers
import dependency_injector.providers as providers
import pymongo
from backend.account import *
import backend.config.core


class Logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)


class MongoDatabases(containers.DeclarativeContainer):
    mongo = pymongo.MongoClient(backend.config.core.MONGODB_URI)
    account_db = mongo.core.account
    google_account_db = mongo.core.google_account

    def __init__(self):
        pass


class MongoDAOs(containers.DeclarativeContainer):
    account_dao = providers.Singleton(AccountDao, account_db=MongoDatabases.account_db, logger=Logger.logger)()
    google_account_dao = providers.Singleton(GoogleAccountDao,
                                             google_account_db=MongoDatabases.google_account_db)()

    def __init__(self):
        pass


class Services(containers.DeclarativeContainer):
    account_logic = providers.Singleton(AccountLogic, account_dao=MongoDAOs.account_dao,
                                        google_account_dao=MongoDAOs.google_account_dao, logger=Logger.logger,
                                        hash_provider=hash_provider)()
    account_service = providers.Singleton(AccountService, account_logic=account_logic)()

    def __init__(self):
        pass


def create_mongodb_indexes():
    MongoDAOs.account_dao.create_indexes()
    MongoDAOs.google_account_dao.create_indexes()
