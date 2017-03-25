import logging
from datetime import datetime

import backend.utils.hash_provider as hash_provider
import dependency_injector.containers as containers
import dependency_injector.providers as providers
import pymongo
from backend.account import *
from backend.login import *
from backend.session import *
import backend.config.core


class Logger():
    logger = None
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)#(logging.DEBUG)


class MongoDatabases(containers.DeclarativeContainer):
    mongo = pymongo.MongoClient(backend.config.core.MONGODB_URI)
    account_db = mongo.core.account
    google_account_db = mongo.core.google_account
    session_db = mongo.core.session

    def __init__(self):
        pass


class MongoDAOs(containers.DeclarativeContainer):
    account_dao = providers.Singleton(AccountDao, account_db=MongoDatabases.account_db, logger=Logger.logger)()
    google_account_dao = providers.Singleton(GoogleAccountDao,
                                             google_account_db=MongoDatabases.google_account_db)()
    session_dao = providers.Singleton(SessionDao, session_db=MongoDatabases.session_db,
                                      logger=Logger.logger)()

    def __init__(self):
        pass


class Services(containers.DeclarativeContainer):
    account_logic = providers.Singleton(AccountLogic, account_dao=MongoDAOs.account_dao,
                                        google_account_dao=MongoDAOs.google_account_dao, logger=Logger.logger,
                                        hash_provider=hash_provider)()
    account_service = providers.Singleton(AccountService, account_logic=account_logic)()

    token_provider = providers.Singleton(DefaultTokenProvider)()
    session_service = providers.Singleton(SessionService, session_dao=MongoDAOs.session_dao,
                                          token_provider=token_provider,
                                          time_provider=datetime, logger=Logger.logger)()

    file_path = backend.config.core.GOOGLE_SECRET_JSON_FILE.format(
        backend.config.core.GOOGLE_LOGIN_CLIENT_ID)
    get_url_path = backend.config.core.GOOGLE_GET_URL_PATH.format(
        backend.config.core.GOOGLE_LOGIN_CLIENT_ID_SHORT)
    google_auth_logic = providers.Singleton(google_auth_logic.AuthLogic,
                                            redirect_url=backend.config.core.REDIRECT_URI,
                                            client_secret_file_path=file_path, client_id_get_url_path=get_url_path,
                                            logger=Logger.logger)()

    auth_logic = providers.Singleton(AuthLogic, hash_provider=hash_provider)
    login_service = providers.Singleton(LoginService, google_auth_logic=google_auth_logic,
                                        session_service=session_service,
                                        account_service=account_service,
                                        auth_logic=auth_logic)()

    def __init__(self):
        pass


def create_mongodb_indexes():
    MongoDAOs.account_dao.create_indexes()
    MongoDAOs.google_account_dao.create_indexes()
    MongoDAOs.session_dao.create_indexes()
