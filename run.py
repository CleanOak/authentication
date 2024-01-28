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

data = user_info.get_all_values()

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


def update_spreadsheet(data):
    try:
        print('Updating user info worksheet.\n')
        update_to_spreadsheet = SHEET.worksheet('user_info')
        update_to_spreadsheet.append_row(data)
        print('worksheet has updated successfully')

    except ValueError as e:
          print(e)


# def add_new_user():
#      print("Adding your account to the system")
#      new_user = SHEET.worksheet("user_info").get_all_values()
#      new_user_row = new_user[-1]

#      user_data = []
#      for user in new_user:
#           user_data.append()
          

                

def signup():
            
            while True:

                new_username = input("Enter your username: \n")
                email_address = input("Enter your email address: \n")           
                new_passwd = input("Enter password: \n")
                conf_passwd = input("Confirm password: \n")
                  
                if conf_passwd == new_passwd:
                    print("Password matched!")
                   
                    print(f'Your username {new_username} and password has been stored successfully!!!')

                    break
                else:
                        print("Please make sure both passwords matches!")

            data = [new_username,email_address,conf_passwd]

            # print(data)

            update_spreadsheet(data)
                           

def main():
     
    answer = userPrompt()

    if answer == 1:
        login(data)

    elif answer == 0:
        signup()


print("LOGIN AUTHENTICATION AND ACCESS CONTROL MODULE\n")

main()




        




