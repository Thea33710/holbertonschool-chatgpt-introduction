class Checkbook:
    """
    A simple checkbook management class that supports deposits, withdrawals,
    and balance checking.
    """

    def __init__(self):
        """
        Initializes a new Checkbook instance with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the current balance.

        Parameters:
        amount (float): The amount of money to deposit (must be non-negative).
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts the specified amount from the balance if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw (must be non-negative).
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop for interacting with the Checkbook. Supports:
    - deposit
    - withdraw
    - balance
    - exit
    """
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be non-negative.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be non-negative.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
