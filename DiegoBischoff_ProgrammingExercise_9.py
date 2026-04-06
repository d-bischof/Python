
class BankAcc:

    name: str
    account_number: int
    amount: float
    interest_rate: float

    def __init__(self, name: str, account_number: int, amount: float, interest_rate: float):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate: float):
        # update the interest rate for this account

        self.interest_rate = new_rate
        print(f"Interest rate for account {self.account_number} has been adjusted to {self.interest_rate:.2f}%.")

    def withdraw(self, amount: float):
        # remove money if the request is valid

        if (amount <= 0):
            print(f"Invalid withdrawal amount for account {self.account_number} Please enter a positive amount.")
            return

        if amount > self.amount:
            print(f"Insufficient funds in account {self.account_number} Withdrawal denied.")
        else:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number} New balance: ${self.amount:.2f}.")

    def deposit(self, amount: float):
        # add money if the deposit amount is positive

        if (amount <= 0):
            print(f"Invalid deposit amount for account {self.account_number} Please enter a positive amount.")
            return

        self.amount += amount
        print(f"Deposited ${amount:.2f} into account {self.account_number} New balance: ${self.amount:.2f}.")

    def get_balance(self):
        # show the current balance

        print(f"Current balance for account {self.account_number}: ${self.amount:.2f}.")

    def calculate_interest(self, days: int):
        # compute interest earned over a period of days

        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        print(f"Interest accrued for account {self.account_number} over {days} days: ${interest:.2f}.")

    def __str__(self):
        return (f"Bank Account\n"
        f"Name: {self.name}\n"
        f"Account Number: {self.account_number}\n"
        f"Balance: ${self.amount:.2f}\n"
        f"Interest Rate: {self.interest_rate * 100:.2f}%")


def main():
    # create an example account and run a few actions

    my_account = BankAcc("Samuel Rodriguez", 1, 1000000.00, 0.07)
    print(my_account)
    print()

    my_account.deposit(500)
    my_account.deposit(100)
    my_account.withdraw(200)
    my_account.withdraw(2000000)
    my_account.get_balance()
    my_account.calculate_interest(30)
    my_account.adjust_interest_rate(0.05)

    print()
    print(my_account)


if __name__ == "__main__":
    main()