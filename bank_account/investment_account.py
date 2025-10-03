from datetime import date, timedelta

from bank_account import BankAccount


class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date(2015, 10, 1)
    __management_fee:float=0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 management_fee: float):
        super().__init__(account_number, client_number, balance, date_created)
        if type(management_fee)==float:
            self.__management_fee = management_fee
        else:
            self.__management_fee=2.55
        self.TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def get_service_charges(self) -> float:
        if self.TEN_YEARS_AGO>=10:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self):
        return_str = super().__str__()
        return_str += "\nDate Created:"+str(self._date_created)
        return_str +=" Management fee:$ %.2f"%(self.__management_fee)
        return_str +=" Account Type: Investment"
        return return_str


c = InvestmentAccount(9483917, 2, 49, date(2025, 8, 10), 1.99)
print(c)