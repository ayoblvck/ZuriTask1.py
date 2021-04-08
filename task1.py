import random
import datetime
date = datetime.datetime.now()
database = {} 
previous_balance = 10000


# Beginning of user experience with ATM
def welcome():
    isValidOptionSelected = False
    print("Welcome to BankPython")
    print(f"The date and time is {date}")

    while isValidOptionSelected == False:
        haveAccount = int(input("do you have an account with us: Enter 1(yes) or 2(no): "))
        if(haveAccount ==1):
            isValidOptionSelected =  True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register()) 
        else:
            print("you have selected an invalid option")

# create an account: Email, First name, last name and password
def register():
    print("********Register********")
    email = input("Enter your email address: ")
    firstName = input("Enter your first name: ").capitalize()
    lastName = input("Enter your last name: ").capitalize()
    password = input("Create new password: ")

    database[accountNumber] = [firstName, lastName, email, password]
    print(f"your account has been created, your account number is {accountNumber}")
    login()


# login to your account: with account number and password
def login():
    isLoginSuccessful = False
    print("Please login!")
    while isLoginSuccessful == False:   
        user_account = int(input("what is your account number: "))
        user_password = input("Enter your password: ")
        if (user_account == accountNumber) and (user_password == database[accountNumber][3]):
           
            print("you have succesfully logged in!!")
            isLoginSuccessful = True
            init_bank_action()
        else:
            print("invalid account number or email address!!!")
            isInputValid = False
            while isInputValid == False:
                user_input = int(input("Type 1 to create an account\nType 2 to try again\n"))
                if user_input == 1:
                    register()
                    isInputValid = True
                elif user_input == 2:
                    login()
                    isInputValid = True
                else:
                    print("invalid selection")
                     

#Generate a random account number    
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)
accountNumber = generateAccountNumber()


# Initial ATM task after successful login
def init_bank_action():
    print(f'Welcome {database[accountNumber][0]} {database[accountNumber][1]}' )
    print("These are the available options: ")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    valid_selection = False
    while valid_selection == False:
        selected_option = (int(input("Please select an option: ")))
        if(selected_option ==1):
            valid_selection = True
            print("you selected the withdrawal option" )
            withdrawal()   
        elif(selected_option ==2):
            valid_selection = True
            print("you selected the deposit option" )
            deposit()
        elif(selected_option == 3):
            valid_selection = True
            print("you selected the complaint option" )
            complaint()
        else:
            print("invalid option selected, please try again")


# Function for withdrawal option
def withdrawal():
    Withdrawal_amount = int(input("how much would you like to withdraw? "))
    print("processing...")
    print("take your cash!!!")
    try_again()
 

# Function for deposit option
def deposit():
    deposit_amount= int(input("how much would you like to deposit: "))
    print("processing...")
    print("your current balance is {}" .format(previous_balance + deposit_amount))
    try_again()


#function for complaint option
def complaint():
    report = input("What issue would you like to report: ")
    print("processing...")
    print("Thank you for contacting us, your report has been recorded and would be looked into!!")
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
        else:
            print("invalid selection, try again!")

welcome()
