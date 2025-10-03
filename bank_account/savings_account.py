from datetime import date

from bank_account import BankAccount


class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.0
    __minimum_balance: float = 0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 minimum_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        if type(minimum_balance) == float:
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 50

    def get_service_charges(self) -> float:
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self):
        return_str = super().__str__()
        return_str += "\nMinimum Balance: $ %.2f Account Type: Saving" % (
            self.__minimum_balance)
        return return_str


