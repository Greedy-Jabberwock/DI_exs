class BankAccount:
    accounts = []

    def __init__(self, balance, username, password):
        self._balance = balance
        self._username = username
        self._password = password
        self._authenticated = False
        BankAccount.accounts.append(self)

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def authenticated(self):
        return self._authenticated

    @property
    def balance(self):
        return self._balance

    @staticmethod
    def _check_value(value):
        if isinstance(value, (int, float)) and value > 0:
            return value
        else:
            raise Exception('Value is not integer or value lesser then 1.')

    def _check_authenticate(self):
        if self._authenticated:
            return True
        else:
            raise Exception('Need authentication.')

    def authenticate(self, username, password):
        if username.lower() == self._username.lower() and password == self._password:
            self._authenticated = True
            print(username)
            print(self.username)
            print(password)
            print(self.password)

    def _deposit(self, value):
        if self._check_authenticate():
            self._balance += self._check_value(value)

    def _withdraw(self, value):
        if self._check_authenticate():
            if self._balance - self._check_value(value) >= 0:
                self._balance -= value
            else:
                print('Balance can\'t be below zero.')


class MinimalBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self._minimum_balance = minimum_balance

    def _withdraw(self, value):
        if self._check_authenticate():
            if self._balance - self._check_value(value) > self._minimum_balance:
                self._balance -= value
            else:
                print('Balance can\'t be below minimal balance.')


class ATM:
    def __init__(self, account_list=None, try_limit=3):
        self.__account_list = self.__check_accounts(account_list)
        self.__try_limit = self.__check_try_limit(try_limit)
        self.__current_tries = 0

    @staticmethod
    def __check_accounts(accounts):
        if accounts is None:
            return []
        for account in accounts:
            if not isinstance(account, (BankAccount, MinimalBalanceAccount)):
                raise TypeError('Wrong type of account in list')
        return accounts

    @staticmethod
    def __check_try_limit(value):
        if isinstance(value, int) and value > 0:
            return value
        else:
            raise TypeError('Wrong try_limit value.')

    def _add_account(self, account):
        if isinstance(account, (BankAccount, MinimalBalanceAccount)):
            self.__account_list.append(account)

    def show_main_menu(self):
        border = '------------------------------------\n'
        print(f'{border}Print username and password to proceed or "0 "\n{border}')
        username = input('Username: ')
        password = input('Password: ')
        self.__log_in(username, password)

    def __username_in_database(self, username):
        for account in self.__account_list:
            if account.username.lower() == username.lower():
                return account
        print('No such user. Try again')
        print('Input 1 for show menu, any button for exit')
        choice = input()
        if choice == '1':
            self.show_main_menu()
        else:
            return None

    def __log_in(self, username, password):
        user = self.__username_in_database(username)
        if user is not None:
            while self.__current_tries < self.__try_limit:
                user.authenticate(username, password)
                if user.authenticated:
                    self.__current_tries = 0
                    self.__show_account_menu(user)
                    break
                else:
                    self.__current_tries += 1
                    username = input('Username: ')
                    password = input('Password: ')
                    continue
            else:
                print('Too many tries.')

    def __show_account_menu(self, account):
        while True:
            border = '------------------------------------\n'
            print(f'{border}'
                  'What do you want to do?\n'
                  '\t1 - deposit\n'
                  '\t2 - withdraw\n'
                  '\t3 - show balance\n'
                  '\t0 - exit\n'
                  f'{border}')
            answer = input()
            if answer in '0123':
                try:
                    answer = int(answer)
                    if answer == 1:
                        print(border)
                        value = input('Sum to deposit: ')
                        print(border)
                        account._deposit(int(value))
                        continue
                    elif answer == 2:
                        print(border)
                        value = input('Sum to withdraw: ')
                        print(border)
                        account._withdraw(int(value))
                        continue
                    elif answer == 3:
                        print(f'{border}Your balance: {account.balance}\n{border}')
                        continue
                    elif answer == 0:
                        print(f'{border}Goodbye!\n{border}')
                        return None
                except TypeError:
                    print('Enter the number 1, 2, 3 or 0.')
                    self.__show_account_menu(account)
                break
            else:
                print('Enter 1 , 2 or 3.')


def main():
    acc1 = BankAccount(1000, 'Jack', 'qwerty123')
    acc2 = MinimalBalanceAccount(5000, 'KowlDron', 'heroOfGods', 200)
    atm = ATM(BankAccount.accounts, 4)
    atm.show_main_menu()


main()
