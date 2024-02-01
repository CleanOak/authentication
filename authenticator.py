import gspread
from google.oauth2.service_account import Credentials
import re
from random import randint



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





Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}


def userPrompt():
     """
     Get user response whether user is an existing on or
     a new user
     """  
     while True:
          
        try:
            
                userAnswer  = input("Do you already have an account? y/n\n")
                if userAnswer.lower() == 'y':
                    return 1
                elif userAnswer.lower() == 'n':
                    return 0

        except:
         print ("Please enter y or n")
          
def login(login_data):
            
            """
            Get existing user credentials to login
            """   
            while True: 

                print("Please enter your details below...\n")           
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


def update_spreadsheet(data):
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
                
                if (re.fullmatch(regex, email_address)):
                    print("Email format accepted")

                    break
                else:
                    print("Please enter a valid email format with the format name@some_address.com")
        
                       
            new_passwd = input("Enter password: \n")
            conf_passwd = input("Confirm password: \n")
                
            if conf_passwd == new_passwd:
                print("Password matched!")
                
                print(f'Your username {new_username} and password has been stored successfully!!!')

                
            else:
                print("Please make sure both passwords matches!")

            data = [new_username,email_address,conf_passwd]

            update_spreadsheet(data)






def main():

    """
    Main function to initalise the whole application
    """
     
    answer = userPrompt()

    if answer == 1:
        login(data)

    elif answer == 0:
        signup()


#print("LOGIN AUTHENTICATION AND ACCESS CONTROL MODULE\n")

#main()






        




