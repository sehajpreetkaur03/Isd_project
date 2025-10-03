"""
File Name : bank_account.py
Author :
created on: 02-Oct-2025
"""
from datetime import date


# declaring BankAccount Class
class BankAccount:
    BASE_SERVICE_CHARGE: float = 0.50
    __account_number: int = 0
    __client_no: int = 0
    __balance: float = 0
    _date_created: date = date.today()

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        self._date_created = date_created

    #propety for account number
    account_number = property(lambda self: self.__account_number)

    # propety for client number
    client_no = property(lambda self: self.__client_number)

    # propety for balance
    balance = property(lambda self: self.__balance)


    def update_balance(self, amount: float):
        self.__balance = self.__balance + amount

    def deposit(self, amount: float):
        self.update_balance(amount)

    def withdraw(self, amount: float):
        self.update_balance(-amount)

    def __str__(self):
        return "Account Number: %d Balance: $ %.2f" % (self.__account_number, self.__balance)


    def get_service_charges(self) -> float:
        return self.BASE_SERVICE_CHARGE

