class BankAccount:
    def __init__(self, username, password, authenticated=False):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):
        if self.username == username:
            if self.password == password:
                self.authenticated = True
            else:
                print('Wrong password.')
                return True
        else:
            print('There is no this username.')
            return False

    def deposit(self, deposit_value):
        if deposit_value > 0 and self.authenticated:
            self.balance += deposit_value
        else:
            raise Exception

    def withdraw(self, withdraw_value):
        if withdraw_value > 0 and self.authenticated:
            self.balance -= withdraw_value
        else:
            raise Exception


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, withdraw_value):
        if self.balance - withdraw_value > self.minimum_balance:
            self.balance -= withdraw_value
        else:
            raise Exception


class ATM:
    def __init__(self, account_list, try_limit):
        self.account_list = filter(lambda x: isinstance(x, BankAccount), account_list)
        try:
            self.try_limit = try_limit
            if try_limit <= 0:
                raise ValueError
        except ValueError:
            self.try_limit = 2
        self.current_tries = 0

    def show_main_menu(self):
        print('Please, log in.')
        may = True
        while may:
            username = input('Enter your username:\n>>>  ')
            password = input('Enter your password:\n>>>  ')
            may = self._log_in(username, password)

    def _log_in(self, username, password):
        if self.current_tries == self.try_limit:
            print('You reached max of tries.')
        for account in self.account_list:
            print(account)
            if account.authenticate(username, password):
                self._show_account_menu(account)
        else:
            self.current_tries += 1

    def _show_account_menu(self, bank_account):
        while True:
            print('1 - deposit\n2 - withdraw\n3 - exit')
            choice = input('Choose option.')
            if choice not in '123':
                continue
            else:
                if choice == '3':
                    break
                else:
                    try:
                        value = int(input('Enter the value:\n'))
                    except TypeError:
                        print('Enter the number.')
                        if choice == '1':
                            bank_account.deposit(value)
                        elif choice == '2':
                            bank_account.withdraw(value)


john = MinimumBalanceAccount('Josh', '1241')
petra = MinimumBalanceAccount('Petra', 'portrait')
kantor = MinimumBalanceAccount('Kantor', 'loreal')
atm = ATM([john, petra, kantor], 5)
atm.show_main_menu()
