import random
import datetime
date = datetime.datetime.now()
database = {} 
previous_balance = 10000


# Beginning of user experience with ATM
def welcome():
    print("Welcome to BankPython")
    print(f"The date and time is {date}")

    while True:
        try:
            haveAccount = int(input("Do you have an account with us: Enter 1(yes) or 2(no): "))
        except:
            print("invalid selection, try again")
        else:
            if(haveAccount ==1):
                False
                login()
            elif(haveAccount == 2):
                False
                register()
            else:
                print("You have selected an invalid option")

# create an account: Email, First name, last name and password
def register():
    print("\n********Register********")
    email = input("Enter your email address: ")
    firstName = input("Enter your first name: ").capitalize()
    lastName = input("Enter your last name: ").capitalize()
    password = input("Create new password: ")

    database[accountNumber] = [firstName, lastName, email, password]
    print(f"Your account has been created!! \nyour account number is {accountNumber}")
    login()


# login to your account: with account number and password
# Excepts valueError
def login():
    isNotValueError = False
    isLoginSuccessful = False
    print("\nPlease login!")
    while isLoginSuccessful == False: 
        while isNotValueError == False:
            try:
                user_account = int(input("Enter your account number: "))
            except ValueError:
                print("Account number should be numbers")
                isNotValueError = False
            else:
                user_password = input("Enter your password: ")
                isNotValueError = True
        if (user_account == accountNumber) and (user_password == database[accountNumber][3]):
            print("You have succesfully logged in!!")
            isLoginSuccessful = True
            init_bank_action()
        else:
            print("Invalid account number or email address!!!")
            while True:
                user_input = int(input("Type 1 to create an account\nType 2 to try again\n"))
                if user_input == 1:
                    register()
                    False
                elif user_input == 2:
                    login()
                    False
                else:
                    print("Invalid selection")
                     

#Generate a random account number    
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)
accountNumber = generateAccountNumber()


#ATM task after successful login: Withdraw, Deposit or Complaint
def init_bank_action():
    print(f'\n** Welcome {database[accountNumber][0]} {database[accountNumber][1]}!!!' )
    print("These are the available options: ")
    print("1. Withdrawal\n2. Cash Deposit\n3. Complaint\n4. Balance")
    valid_selection = False
    while valid_selection == False:
        selected_option = (int(input("Please select an option: ")))
        if(selected_option ==1):
            valid_selection = True
            print("You selected the withdrawal option" )
            withdrawal()   
        elif(selected_option ==2):
            valid_selection = True
            print("You selected the deposit option" )
            deposit()
        elif(selected_option == 3):
            valid_selection = True
            print("You selected the complaint option" )
            complaint()
        elif(selected_option == 4):
            valid_selection = True
            print("You selected the balance option" )
            balance()
        else:
            print("invalid option selected, please try again")


# Function for withdrawal option
def withdrawal():
    global previous_balance
    Withdrawal_amount = int(input("How much would you like to withdraw (in figures)? "))
    previous_balance -= Withdrawal_amount
    print("Processing...")
    print("Take your cash!!!")
    try_again()
 

# Function for deposit option
def deposit():
    global previous_balance
    deposit_amount= int(input("How much would you like to deposit (in figures): "))
    previous_balance += deposit_amount
    print("Processing...")
    print(f"Deposit of N{deposit_amount} was successful!")
    try_again()


#function for complaint option
def complaint():
    report = input("What issue would you like to report: ")
    print("Processing...")
    print("Thank you for contacting us, your report has been recorded and would be looked into!!")
    try_again()
    

#function prints the current balance
def balance():
    print(f"Your current balance is N{previous_balance}")
    try_again()

# To carry out another transaction: have to reenter password
def try_again():
    isValidOptionSelected = False
    while isValidOptionSelected == False:
        another_transaction = int(input("Do you want to carry out another transaction? 1(yes) or 2(no)? "))
        if another_transaction == 1:
            password2 = input("please reenter password: ")
            if password2 == database[accountNumber][3]:
                init_bank_action()
                isValidOptionSelected = True
            else:
                print("wrong password!")
        elif another_transaction == 2:
            print("Thank you and have a nice day!")
            isValidOptionSelected = True
            exit()
        else:
            print("invalid selection, try again!")

welcome()