class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = "1234"
        self.is_authenticated = False

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
        else:
            print(f"The pin {input_pin} is not valid. Please Try again.")
    def check_balance(self):
        if self.is_authenticated:
            print(f"Your current balance is {self.balance:.2f}Rs")
        else:
            print("Please Verify your PIN first.")
    def deposit(self, amount):
        if self.is_authenticated:
            if amount >= 0:
                self.balance += amount
                print(f"Transaction Successful.You have successfully desposited the amount{amount:.2f}Rs")
                print(f"Your Current balance is now {self.balance}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("PLease verify your pin first.")


    def withdram(self, amount):
        if self.is_authenticated:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw Successful, You have successfully withdraw the {amount:.2f}")
                print(f"Your Current amount is {self.balance}")
            else:
                print("Withdraw amount must be positive.")
        else:
            print("Please Verify your pin first.")


    def exit(self):
        print("Thank you for using the ATM. Goodbye!")

        return False
    

    def menu(self):
        print("=====wELCOME TO THE ATM SYSTEM=====")
        
        attempts = 0
        while attempts < 3 and not self.is_authenticated:
            input_pin = input("Enter your 4-digit PIN: ").strip()
            if not input_pin.isdigit() or len(input_pin) != 4:
                print("❌ PIN must be exactly 4 digits.")
                attempts += 1
                continue
            if not self.check_pin(input_pin):
                attempts += 1
        if not self.is_authenticated:
            print("❌ Maximum PIN attempts exceeded. Exiting.")
            return

        while True:
            print("====ATM MACHINE SYSTEM====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter Your choice (1, 2 , 3, 4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter the AMOUNT you want to DEPOSIT: "))
                    self.deposit(amount)
                except ValueError:
                    print("Please Enter Valid Amount")
            elif choice == "3":
                try:
                    amount = float(input("Enter the AMOUNT you want to Withdraw: "))
                    self.withdram(amount)
                except ValueError:
                    print("Please Enter Valid Amount")
            elif choice == "4":
                if not self.exit():
                    break
            else:
                print("Invalid Selection, Please select the right option.")
            

if __name__ == "__main__":
    try:
        atm = ATM()
        atm.menu()
    except Exception as e:
        print(f"Fatal error: {e}")

