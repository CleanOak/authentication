# import from python library
import re

# imports from google librabry
import gspread
from google.oauth2.service_account import Credentials





SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCPOED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCPOED_CREDS)
SHEET = GSPREAD_CLIENT.open('Authenticate')

user_info = SHEET.worksheet('user_info')

def login_data():
    """
    Function to allow existing users to login
    """
    data = user_info.get_all_values()
    return data

          
def login(login_user_data): 
    """
    Get existing user credentials to login
    """  
    while True:

        print("Please enter your details below to login...\n")           
        user_name = input("Enter your username: \n")
        passwd = input("Enter password: \n")
        try:
            for creds in login_user_data:
                if (user_name in creds[0] and passwd in creds[2]):
                    user1 = creds[0]
                    passwd1 = creds[2]
            if (user1 == user_name and passwd1 == passwd):
                print ("You have logged in sucessfully\n")

                break                                
        except ValueError as v:
            print("Your username or password does not match please try again\n", v)


def update_spreadsheet(data):
    """
     Function to update google spreadsheet with user credentials
    """
    try:
        print('Updating user info worksheet.\n')
        update_to_spreadsheet = SHEET.worksheet('user_info')
        update_to_spreadsheet.append_row(data)
        print('worksheet has updated successfully')

    except ValueError as e:
        print(e)


def signup():
    """
    Get new user details to create login credentials 
    """
    while True:
        print("Follow the prompts to save your user information...\n")
        new_username = input("Enter your username: \n")

        print("Please enter an email with the format name@some_address.com")
        email_address = input("Enter your email address: \n")   

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email_address):
            print("Email format accepted")

            break
        else:
            print("Please enter a valid email format with the format name@some_address.com")

    new_passwd = input("Enter password: \n")
    conf_passwd = input("Confirm password: \n")
        
    if conf_passwd == new_passwd:
        print("Password matched!")
        
        print(f'Your username {new_username} and password has been stored successfully!!!\n')

    else:
        print("Please make sure both passwords matches!")

    data = [new_username,email_address,conf_passwd]

    update_spreadsheet(data)













        




