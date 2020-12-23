import json
import pathlib
import random
import jsonpickle

class BankAccount:
    
    def __init__(self, ssn, balance=0):
        self._ssn = ssn
        self._balance = balance

    @property    
    def ssn(self):
        return self._ssn

    @property
    def balance(self):
        return self._balance  

    @staticmethod
    def authentication(filename, ssn, account_number):
        '''
        Read JSON file and checks whether account number is valid
        '''

        with open(filename, "r") as json_file:
            data = json.load(json_file)
            stem = pathlib.Path(filename).stem
            accounts = data[stem]

            # Using ssn and account number check whether account number is valid or not
            for account in accounts:
                account = jsonpickle.decode(account)
                if account.ssn == ssn and account.account_number == account_number:
                    return True

            return False

class CheckingAccount(BankAccount):
    
    def __init__(self, ssn, balance):
        super().__init__(ssn, balance)
        self._account_type = 'Checking'
        self._account_number = random.randint(10000, 99999)

    @property
    def account_type(self):
        return self._account_type

    @property
    def account_number(self):
        return self._account_number

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        if deposit > 0:
            self._deposit = deposit
            self._deposit += 1
            self._balance += self._deposit
        else:
            raise ValueError

    @property
    def withdrawal(self):
        return self._withdraw

    @withdrawal.setter
    def withdrawal(self, withdraw):
        if withdraw > 0:
            self._withdraw = withdraw
            self._balance -= self._withdraw
        else:
            raise ValueError

class SavingsAccount(BankAccount):
    
    def __init__(self, ssn, balance):
        super().__init__(ssn, balance)
        self._account_type = "Savings"
        self._account_number = random.randint(100000, 200000)

    @property
    def account_type(self):
        return self._account_type

    @property
    def account_number(self):
        return self._account_number

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        if deposit > 0:
            self._deposit = deposit
            self._deposit += 5
            self._balance += self._deposit
        else:
            raise ValueError

    @property
    def withdrawal(self):
        return self._withdraw

    @withdrawal.setter
    def withdrawal(self, withdraw):
        if withdraw > 0:
            self._withdraw = withdraw
            self._balance -= self._withdraw
        else:
            raise ValueError