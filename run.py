import gspread
from google.oauth2.service_account import Credentials
import re
# from distutils.util import strtobool as stb 
import setuptools
import sys


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

def userPrompt():
     """
     Get user response
     """
     
     try:
          
            userAnswer  = input("Are you a new or existing user? y/n\n")
            if userAnswer.lower() == 'y':
                return 1
            elif userAnswer.lower() == 'n':
                return 0
          
     except ValueError:("Please enter y or n")
          
          
   


def login(login_data):
            
            """
            Get user credentials to login
            """   
            while True: 

                user_name = input("Enter your username: \n")
                passwd = input("Enter password: \n")
                try:
                    for creds in login_data:
                        if (user_name in creds[0] and passwd in creds[2]):  
                            user1 = creds[0]
                            passwd1 = creds[2]
                
                    if (user1 == user_name and passwd1 == passwd):
                        print ("You have logged in sucessfully")

                        break
                                
                except:
                    print("Your username or password does not match please try again\n")


def update_spreadsheet(data, worksheet):
     
     print(f'Updating {worksheet} worksheet.\n')
     update_to_spreadsheet =  SHEET.worksheet(worksheet)
     update_to_spreadsheet.append_row(data)
     print(f'{worksheet} worksheet has updated successfully')
                

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

answer = userPrompt()

if answer == 1:
     login(data)

elif answer == 0:
    print("please sign up")




        




