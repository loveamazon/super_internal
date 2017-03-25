import account_error_code
from account_model import AccountInfo


class AccountLogic:
    def __init__(self, account_dao, google_account_dao, hash_provider, logger):
        self.account_dao = account_dao
        self.google_account_dao = google_account_dao
        self.logger = logger
        self.hash_provider = hash_provider

    def get_account_info(self, request):
        return self.account_dao.get_account_by_name(request.name)

    def __insert_account(self, name, password, email, display_name):
        password_hashed = password
        if password is not None:
            password_hashed = self.hash_provider.hash_str(password.encode('utf-8'))
        return self.account_dao.insert_account(name, password_hashed, display_name, email)

    def register_account(self, register_account_request):
        code, user_id = self.__insert_account(register_account_request.name, register_account_request.password,
                                              register_account_request.email,
                                              register_account_request.display_name)
        account_info = None
        if code == account_error_code.OK:
            account_info = AccountInfo(str(user_id), register_account_request.name,
                                       register_account_request.display_name,
                                       register_account_request.email,
                                       None)

        return code, account_info

    def register_google_account(self, register_account_request):
        google_account = self.google_account_dao.get_account(register_account_request.external_user_id)
        if google_account is None:
            code, user_id = self.__insert_account("[google]#{}".format(register_account_request.external_user_id),
                                                  None,
                                                  register_account_request.email,
                                                  register_account_request.display_name)
            if code == account_error_code.OK:
                # TD duplicated check, in concurrent access, it could happen.
                self.google_account_dao.insert_account(register_account_request.external_user_id,
                                                       register_account_request.name,
                                                       register_account_request.display_name,
                                                       register_account_request.title,
                                                       register_account_request.email, user_id)
            elif code == account_error_code.DUPLICATED:
                self.logger.error(
                    "The google account already has ccp account registered! The google player id %s, " +
                    "name %s, the user id %s",
                    register_account_request.external_user_id, register_account_request.name, user_id)
            else:
                raise Exception("The code not handled")

            account_info = AccountInfo(user_id, register_account_request.name, register_account_request.display_name,
                                       register_account_request.email,
                                       register_account_request.external_user_id)
        else:
            code = account_error_code.DUPLICATED
            account_info = AccountInfo(google_account.user_id, google_account.name,
                                       google_account.display_name,
                                       google_account.email,
                                       google_account.external_user_id)
        return code, account_info
