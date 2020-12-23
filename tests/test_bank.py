import random
import pytest

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

###########################################################

def test_BankAccount():
    '''
    Test for bank account
    '''

    bank_account = BankAccount("111223333", 100)
    assert bank_account.ssn == "111223333"
    assert bank_account.balance == 100

    with pytest.raises(AttributeError):
        bank_account.ssn = "123456789"
        
    with pytest.raises(AttributeError):
        bank_account.balance = 20

###########################################################

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

###########################################################

def test_CheckingAccount():
    '''
    Test for checking account
    '''

    checking_account = CheckingAccount("222336789", 100)

    assert checking_account.ssn == "222336789"
    assert checking_account.balance == 100
    assert checking_account.account_type == "Checking"
    assert checking_account.account_number != None and isinstance(checking_account.account_number, int)

    checking_account.deposit = 10
    assert checking_account.balance == 111

    checking_account.withdrawal = 20
    assert checking_account.balance == 91
    
    with pytest.raises(AttributeError):
        checking_account.balance = 100

    with pytest.raises(AttributeError):
        checking_account.account_type = "Savings"

    with pytest.raises(AttributeError):
        checking_account.account_number = 192029330

    with pytest.raises(ValueError):
        checking_account.deposit = -10

    with pytest.raises(ValueError):
        checking_account.withdrawal = -90


###########################################################

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

###########################################################

def test_SavingsAccount():
    '''
    Test for savings account
    '''

    savings_account = SavingsAccount("10001", 20)

    assert savings_account.ssn == "10001"
    assert savings_account.balance == 20
    assert savings_account.account_type == "Savings"
    assert savings_account.account_number != None and isinstance(savings_account.account_number, int)

    savings_account.deposit = 10
    assert savings_account.balance == 35

    savings_account.withdrawal = 5
    assert savings_account.balance == 30
    
    with pytest.raises(AttributeError):
        savings_account.account_type = "Savings"

    with pytest.raises(AttributeError):
        savings_account.account_number = 192029330

    with pytest.raises(ValueError):
        savings_account.deposit = -10

    with pytest.raises(ValueError):
        savings_account.withdrawal = -90