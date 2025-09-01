class Checkbook:
    def __init__(self):
        """
        Initialise le solde du compte à 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Ajoute un montant au solde du compte.
        
        Args:
            amount (float): Montant à déposer.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du solde si les fonds sont suffisants.
        
        Args:
            amount (float): Montant à retirer.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale qui gère l'interaction utilisateur pour 
    déposer, retirer, consulter le solde ou quitter.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()