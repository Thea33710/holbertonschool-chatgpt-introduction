#!/usr/bin/python3


# Classe représentant un simple chéquier
class Checkbook:
    def __init__(self):
        # Initialisation du solde à 0
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte si les fonds sont suffisants
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel
        """
        print("Current Balance: ${:.2f}".format(self.balance))


# Fonction principale qui exécute le programme
def main():
    cb = Checkbook()
    while True:
        # Demande à l'utilisateur l'action à effectuer
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )
        action = action.lower()

        if action == 'exit':
            # Quitte le programme
            break

        elif action == 'deposit':
            # Effectue un dépôt après validation
            try:
                amount = float(input("Enter the amount to deposit: $"))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            cb.deposit(amount)

        elif action == 'withdraw':
            # Effectue un retrait après validation
            try:
                amount = float(input("Enter the amount to withdraw: $"))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            cb.withdraw(amount)

        elif action == 'balance':
            # Affiche le solde
            cb.get_balance()

        else:
            # Commande invalide
            print("Invalid command. Please try again.")


# Point d'entrée du script
if __name__ == "__main__":
    main()
