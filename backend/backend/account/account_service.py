class AccountService:
    def __init__(self, account_logic):
        self.account_logic = account_logic

    def get_account_info(self, request):
        return self.account_logic.get_account_info(request)

    def register_account(self, register_account_request):
        return self.account_logic.register_account(register_account_request)

    def register_google_account(self, register_account_request):
        return self.account_logic.register_google_account(register_account_request)
