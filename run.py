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


    
    

def login(login_data):
            
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
                    
                    print("Your details do not match please sign up")
                
            
                                  
login(data)
#print(data)

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
        




