class BankingSystem:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def check_balance(self):
        print(f"\nYour current balance is: M{self.balance:.2f}")
        
    def deposit_money(self):
        try:
            amount = float(input("\nEnter amount to deposit (M): "))
            if amount <= 0:
                print("Please enter a positive amount.")
                return
            
            previous_balance = self.balance
            self.balance += amount
            self.transactions.append(f"Deposited: M{amount:.2f}")
            
            print("\n===== DEPOSIT CONFIRMATION =====")
            print(f"Amount deposited: M{amount:.2f}")
            print(f"Previous balance: M{previous_balance:.2f}")
            print(f"Current balance: M{self.balance:.2f}")
            print("================================")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def withdraw_money(self):
        try:
            amount_withdrawn = float(input("\nEnter amount to withdraw (M): "))
            if amount_withdrawn <= 0:
                print("Please enter a positive amount.")
                return
                
            if amount_withdrawn > self.balance:
                print("Insufficient funds. Withdrawal failed.")
                print(f"Your current balance is: M{self.balance:.2f}")
                return
            
            previous_balance = self.balance
            self.balance -= amount_withdrawn
            self.transactions.append(f"Withdrew: M{amount_withdrawn:.2f}")
            
            print("\n===== WITHDRAWAL CONFIRMATION =====")
            print(f"Amount withdrawn: M{amount_withdrawn:.2f}")
            print(f"Previous balance: M{previous_balance:.2f}")
            print(f"Current balance: M{self.balance:.2f}")
            print("===================================")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def view_transaction_history(self):
        if not self.transactions:
            print("\nNo transactions to display.")
            return
            
        print("\n===== Transaction History =====")
        for transaction in self.transactions:
            print(transaction)
        print("==============================")
        print(f"Current total balance: M{self.balance:.2f}")

def main():
    bank = BankingSystem()  #bank is an Object of BankingSystem class
    
    while True:
        # print("\n===== WELCOME TO SNAKE BANK =====") 
        # print("1. Check Balance")
        # print("2. Deposit Money")
        # print("3. Withdraw Money")
        # print("4. View Transaction History")
        # print("5. Exit")
        # print("===============================")
        
        print("""   
                 1. Check Balance 
                 2. Deposit Money
                 3. Withdraw Money
                 4. View Transaction History
                 5. Exit
                 ===============================""")
        try:
            choice = int(input("Please select an option (1-5): "))
            
            match choice:
                case 1:
                    bank.check_balance()
                case 2:
                    bank.deposit_money()
                case 3:
                    bank.withdraw_money()
                case 4:
                    bank.view_transaction_history()
                case 5:
                    print("\nThank you for using Snake Bank. Goodbye!")
                    break
                case _:
                    print("\nInvalid option. Please select a number between 1 and 5.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    main()