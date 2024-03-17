# import from python library
import re
import time


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


def update_spreadsheet(data):
    """
     Function to update google spreadsheet with user credentials
    """
    print('Updating user info worksheet.\n')
    user_info.append_row(data)
    time.sleep(0.5)
    print('worksheet has updated successfully\n')

          
def login(login_user_data):
    """
    Get existing user credentials to login
    """
    x=0
    while x==0:
        print("Please enter your details below to login to the game....\n")

        # while True:
        user_name = input("Enter your username: \n")            
        passwd = input("Enter password: \n")
        try:
            for data in login_user_data:
                if user_name == data[0]:
                    if  passwd == data[2]:
                        print(f"Hello {user_name}, you have logged in sucessfully...")
                        x= 1
                    else:
                        print("Incorrect password...")
        except ValueError as v:
            print("Your username or password does not match please try again\n", v)

def signup(user_data):
    """
    Get new user details to create login credentials 
    """
    while True:
        print("Follow the prompts to Sign up...\n")
        new_username = input("Enter your username: \n") 
        try:

            for data in user_data:
                if new_username == "":
                    print("Please enter a valid value for the username\n")
                    break
        except ValueError as v:
            print("Please enter a valid value for the username\n")
        #         if new_username == data[0]:
        #             print("User exists please use a differnt username\n")
        #             time.sleep(0.5)
        #             signup(login_data())
        #             break    
            print("Please enter an email with the format name@some_address.com")
            email_address = input("Enter your email address: \n")
            regex = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,7}\b'
        
        if re.fullmatch(regex, email_address):
                
            print("Email format accepted\n")
            break
            
        else:
            print("Please enter a valid email format with the format name@some_address.com")
    while True:
        print("Your password must be 8 characters long, must contain a capital letter(s),")
        print("small letter(s) and at least a number and special characters")
        print("For example:XdsE83&! \n")
        new_passwd = input("Enter password:\n")
        
        #compiling regex
        reg_pass = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$'
        match_re = re.compile(reg_pass)

        # searching regex
        reg_search = re.search(match_re, new_passwd)

        #validating conditions
        if reg_search:
            print("Password is valid")
            break
        else:
            print("Password is invalid")

    conf_passwd = input("Confirm password: \n")
    if conf_passwd == new_passwd:
        print("Password matched!\n")
        print(f'Your username {new_username} and password has been stored successfully!!!\n')

    else:
        print("Please make sure both passwords matches!")

    data = [new_username,email_address,conf_passwd]
    update_spreadsheet(data)
