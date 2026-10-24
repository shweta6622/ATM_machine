# ================================
#         ATM MACHINE
# ================================

import getpass
YELLOW_BOLD = "\033[1;4;33m"
GREEN_BOLD = "\033[1;4;32m"
RESET = "\033[0m"
print(f"{YELLOW_BOLD}Welcome to SBI ATM{RESET}".center(80))
pin = "2026"
attempts = 0
balance = 5000

# ----------- CARD -----------------
card=input(f"{GREEN_BOLD}Insert your card{RESET}:")
while card.lower() != "sbi debit card":
    print("Wrong card name")
    card = input("Insert your card:")
print("Card Accepted")



# ----------- PIN -------------------
while attempts < 3:
    user_pin=getpass.getpass("enter PIN:")
    if user_pin == pin:
        print("PIN verified successfully!")
        print("Account Holder:", "Shweta Prajapati")
        break
    else:
        attempts +=1
        print("Wrong PIN! Please Try again.")
        if attempts < 3:
            print("Attempts left:", 3 - attempts)
if attempts == 3 and user_pin!= pin:
    print("Too many wrong attempts!")
    print("Card blocked!")
else:



# ------------ ATM OPTION ----------------
    while True:
        print("1)check balance\n2)withdra money\n3)deposit money\n4)exit")
        user_selection=int(input("select the option:"))
        if user_selection==1:
            print("your balance is",balance)
        elif user_selection==2:
            user_amount=int(input("enter amount to withdraw:"))
            balance = balance - user_amount
            print("your new balance is:", balance)
        elif user_selection==3:
            deposite = int(input("enter amount to deposite:"))
            balance = balance + deposite
            print("Money deposited seccessfully!")
            print("Your new balance is:", balance)
        elif user_selection==4:
            print("Thankyou for using ATM!")
            break
        else:
            print("exit")
    
