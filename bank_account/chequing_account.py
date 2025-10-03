from datetime import date

from bank_account import BankAccount


class ChequingAccount(BankAccount):
    __overdraft_limit: float = 0
    __overdraft_rate: float = 0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        #check whether overdraft limit can be converted into float
        if type(overdraft_limit) == float:
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100
        if type(overdraft_rate) == float:
            self.__overdraft_rate = overdraft_rate
        else:
            self.__overdraft_rate = 0.05

    def __str__(self):
        return_str = super().__str__()
        return_str +="\nOverdraft Limit: $ %.2f Overdraft Rate: %.2f %% Account Type: Chequing" % (self.__overdraft_limit,self.__overdraft_rate)
        return return_str

    def get_service_charges(self) -> float:
        print("Overdraft limit:%d" % self.__overdraft_limit)
        print("Balance :%d" % self.balance)
        if self.balance>=self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance)
        else:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate/100


#This for testing this class
c = ChequingAccount(1234, 1, -600, date(2025,10,1), -100, 5.0)
print(c)
print("Calculated Service Charges=$ %0.2f" % c.get_service_charges())

c1 = ChequingAccount(1235, 1, -100, date(2025,10,1), -100, 5.0)
print(c1)
print("Calculated Service Charges=$ %0.2f" % c1.get_service_charges())
