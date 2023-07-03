# 밖에서 바로 호출 못하도록 __ 걸어줌
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance
    
    def doposit(self, amount):
        self.__balance += amount

    # get_balance로 접근해야지만 balance로 접근가능함.
    def get_balance(self):
        return self.__balance
    
account = BankAccount('12345678', 1000000)
print(account._account_number)
print(account.get_balance())