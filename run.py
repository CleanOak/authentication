import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCPOED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCPOED_CREDS)
SHEET = GSPREAD_CLIENT.open('Authenticate')

#user_info = SHEET.worksheet('user_info')

#data = user_info.get_all_values()

print("LOGIN AUTHENTICATION AND ACCESS CONTROL MODULE\n")


def signup():
    while True:

            user_name = input("Enter your username: \n")
            email = input("Enter email address: \n")
            pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(pattern, email):
                 print("This is correct")
        
                 
            passwd = input("Enter password: \n")
            conf_passwd = input("Confirm password: \n")

            if conf_passwd == passwd:

                print("You have registered successfully!")

            else:
                print("Password is not the same as above!")

signup()
        




