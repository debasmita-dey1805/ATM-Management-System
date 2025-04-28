class CardHolder:
    def __init__(self,name,pin,card_number,balance=0):
        self.__name=name
        self.__pin=pin
        self.__card_number=card_number
        self.__balance=balance

    # Getter Method
    def get_name(self):
        return self.__name
    def get_pin(self):
        return self.__pin
    def get_card_number(self):
        return self.__card_number
    def get_balance(self):
        return self.__balance
        
    # Setter method
    def set_balance(self,amount):
        self.__balance=amount
    def set_pin(self, new_pin):
        self.__pin = new_pin

class ATM:
    def __init__(self):
        self.card_holders={}
    
    def add_card_holder(self,card_holder):
        self.card_holders[card_holder.get_card_number()]=card_holder
    
    def authenticate_user(self,card_number,pin):
        holder=self.card_holders.get(card_number)
        if holder and holder.get_pin() ==pin:
            return holder
        else:
            return None     
    
    def change_pin(self,card_holder,new_pin):
        if len(new_pin)!=4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
            return
        card_holder.set_pin(new_pin)
        print("PIN successfully updated!")
    
    def transfer_money(self,sender,receiver_card_number,amount):
        receiver=self.card_holders.get(receiver_card_number)
        if not receiver:
            print("Receiver not found.")
            return
        if amount <=0:
            print("AMount must be greater than Zero .")
            return
        if sender.get_balance() >=amount:
            sender.set_balance(sender.get_balance()-amount)   
            receiver.set_balance(receiver.get_balance()+amount)
            print(f"Successfully transferred Rs.{amount:.2f} to {receiver.get_name()}.")
            print(f"Your new balance is: Rs.{sender.get_balance():.2f}")
        else:
            print("Insufficient balance to transfer .")

    def deposit(self,card_holder,amount):
        if amount <=0:
            print("Amount must be gretter than zero. ")
            return
        card_holder.set_balance(card_holder.get_balance()+amount)
        print(f"Successfully deposited Rs.{amount:.2f}. New Balance: Rs.{card_holder.get_balance():.2f}")

    def withdraw(self,card_holder,amount):
        if amount <=0:
            print("Amount must be greater than zero.")
            return
        if card_holder.get_balance()>=amount:
            card_holder.set_balance(card_holder.get_balance()-amount) 
            print(f"Successfully withdraw Rs.{amount:.2f}.Remaining Balance:Rs.{card_holder.get_balance():.2f}")
        else:
            print("Insufficient Balance.")
    def check_balance(self,card_holder):
        print(f"Your current balance is :Rs.{card_holder.get_balance():.2f}")

def main():
    atm=ATM()

    atm.add_card_holder(CardHolder("John", "1232", "12321234", 500.0))
    atm.add_card_holder(CardHolder("Bobby", "4365", "43456756", 1500.0))
    atm.add_card_holder(CardHolder("Parul", "9876", "98098798", 750.0))


    print("Welcome to the XYZ ATM Machine!")
    attempts=0
    while attempts <3:
        card_number =input("Enter your card number: ").strip()
        pin=input("Enter your PIN: ").strip()

        user=atm.authenticate_user(card_number,pin)
        if user:
            print(f"Welcome , {user.get_name()}!")

            while True:
                print("\nPlease select an option:")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Check Balance")
                print("4.Change PIN")
                print("5.Transfer Money")
                print("6.Exit")
                choice=input("Enter choice(1-6): ").strip()

                if choice =="1":
                    try:
                        amount=float(input("Enter amount to deposit: "))
                        atm.deposit(user,amount)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif choice =="2":
                    try:
                        amount=float(input("Enter amount to withdraw: "))
                        atm.withdraw(user,amount)  
                    except ValueError:
                        print("Invalid input. Please enter a number. ")
                elif choice =="3":
                    atm.check_balance(user)
                elif choice =="4":
                    new_pin=input("Enter new 4-digit PIN: ").strip()
                    atm.change_pin(user,new_pin)
                elif choice =="5":
                    receiver_card=input("Enter receiver's card number: ").strip()
                    try:
                        amount=float(input("Enter amount to transfer: "))
                        atm.transfer_money(user,receiver_card,amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")    
                elif choice =="6":
                    print(f"Thankyou for using the ATM. Goodbye, {user.get_name()}!")
                    return
                else:
                    print("Invalid choice. Please select from 1-6.")
        else:
            print("Authentication Failed. please try again.")
            attempts +=1       
    print("\nToo many failed attempts.")
if __name__=="__main__":
    main()                                   






