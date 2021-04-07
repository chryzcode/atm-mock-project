from datetime import datetime
import random

database = {}

now = datetime.now()
currentday = now.strftime("%d of %B, %Y.")
currenttime = now.strftime("%H:%M:%S")

def generatedaccountnumber():
    return random.randrange(1111111111, 9999999999)

def login():
    print('== === *** Login Page *** === ==\n')
    print('Enter your account details below!\n')
    accountnumberfromuser = int(input('Please put in your registered account number: \n'))
    password = input('Put in your password carefully: \n')

    for accountnumber, userdetails in database.items():
        if(accountnumber == accountnumberfromuser):
            if (userdetails[3] == password):
                bankoperation(userdetails)
                isloginsuccessful = True
            else:
                print('\nInvalid account or password')
                login()
        else:
            print('\nInvalid account or password')
            login()

def bankoperation(user):

    print(f'=== == Welcome %s , You logged in on the {currentday} {currenttime}  == ===\n'%user[1])
    selectedoption = int(input('=== == What would you like to do or assist you with? == ===\n(1) Withdrawal\n(2) Deposit\n(3) Complaint\n(4) Logout\n(5) Exit\n'))
    if (selectedoption == 1):
        withdrawal()
    elif (selectedoption == 2):
        deposit()
    elif (selectedoption == 3):
        complaint()
    elif (selectedoption == 4):
        logout()
    elif (selectedoption == 5):
        exit()
    else:
        print('Invalid option')
        bankoperation()

def register():
    print('\n== === *** Register Here With Us *** === ==\n')
    first_name = input('Fill in your first name: \n')
    last_name = input('Fill in your last name: \n')
    email = input('Input your E-mail address: \n')
    password = input('Generate your password: \n')
    accountnumber = generatedaccountnumber()
    print(f'=== == --- Welcome, you have an account created on the {currentday} {currenttime} --- === ==\n')
    print('=== == Here is your account number ***%d*** == ===\n' %accountnumber)
    print('== -- Keep your details a secret, most especially your **account number** and **password** -- ==\n')
    database[accountnumber] = [first_name, last_name, email, password]
    login()



def withdrawal():
    money = input('How much would you like to withdraw: \n')
    print('Here is it, take your cash: %s ' %money)
    done()

def deposit():
    deposit = input('How much would you like to deposit: \n' )
    print('Current balance: %s '%deposit)
    done()

def complaint():
    comlaint = input('What issue will you like to report?: \n' )
    print('Thank you for contacting us.')
    done()

def done():
    print('\nHi, would you love to do anything else or logout.\n')
    choose = int(input('Press 1 to continue\nPress 2 to logout\n'))
    if (choose == 1):
        do = int(input('Welcome back for another transaction\n(1) Withdrawal\n(2) Deposit\n(3) Complaint\n'))
        if (do  == 1):
            withdrawal()
        elif (do  == 2):
            deposit()
        elif (do == 3):
            complaint()
        else:
            print('Invalid option')
            done()

    elif (choose == 2):
        print('Okay, bye for now')
        logout()
    else:
        print('Invalid input')
        done()

def logout():
    login()

def exit():
    exit()


register()
