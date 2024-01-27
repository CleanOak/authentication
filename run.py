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

user_info = SHEET.worksheet('user_info')

data = user_info.get_all_values()

print("LOGIN AUTHENTICATION AND ACCESS CONTROL MODULE\n")


    
    

def login(data):
    user_name = input("Enter your username: \n")
    passwd = input("Enter password: \n")

    for x in data:
        if (user_name == x[0] and passwd == x[2]):
            print("Login succesful")
                   
                
        else:
         print("Username or password incorrect")
        
    


login(data)







# def signup():
#     while True:

#             user_name = input("Enter your username: \n")
#             email = input("Enter email address: \n")             
#             passwd = input("Enter password: \n")
#             conf_passwd = input("Confirm password: \n")

#             if conf_passwd == passwd:
#                 print("You have registered successfully!")
#             else:
#                 print("Password is not the same as above!")

# signup()
        




