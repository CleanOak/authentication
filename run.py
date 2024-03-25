# imports from python library
import time
import os


# internal imports from exiting python file
from authenticator import login
from authenticator import signup
from authenticator import login_data
from game import choose_level



def app_banner():
    """
    function to display banner for the game for the application
    """
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("*** WELCOME TO THE COUNTRIES GUESSING GAME ***")
    print("+++++++++++++++++++++++++++++++++++++++++++\n")

def game_banner():
    """
    Function to display the game and rules
    """
    print("++++++++++++++++++++++++++++++++++++")
    print("*** BRING ON YOUR BEST COUNTRY KNOWLEDGE ***")
    print("++++++++++++++++++++++++++++++++++++\n\n")
    print("*** RULES OF THE GAME***")
    time.sleep(0.5)
    print("In this game, there is a list of countries present")
    time.sleep(0.5)
    print("User will guess a random letter to guess the country")
    time.sleep(0.5)
    print("User has 10 tries to guess the correct country word")
    time.sleep(0.5)
    print("If the random alphabet is in the country word, user receives a correct prompt")
    time.sleep(0.5)
    print("If the letter is wrong and not in the country word the number of tries reduces until zero\n\n")

    print("Game Starts Now...")
    
def login_check():
    """
    Function to validate if user needs a new account or not
    """
    while True:

        user_answer  = input("Do you already have an account? y/n\n")
        if user_answer.lower() == 'y':
            user_exist()
            break
        if user_answer.lower() == 'n':
            new_user()
            break
        else:
            print ("Please enter y or n")

def user_exist():
    """
    Funtion to check if user already has login details
    """
    login(login_data())
    game_banner()

def new_user():
    """
    Function to allows new user to create username and password
    """
    signup(login_data())
    login(login_data())
    game_banner()

def restart_game():
    """
    Function to ask user if they want to play again
    and restart the game and if not exit the terminal
    """
    while True:
        answer = input("\nDo you want to play again?: Y/N\n")
        os.system('clear')
        if answer.upper() == "Y":
            print("\nTRY YOUR LUCK AGAIN!!")
            print("\nRestarting Game......")
            time.sleep(1)
            print("Game Started")
            time.sleep(1)
            game_banner()
            choose_level()
        elif answer.upper() == "N":
            time.sleep(1.5)
            print("\nGood Bye!!")
            time.sleep(1)
            print("\nLogging out......")
            time.sleep(1)
            print("\nYou have successfully logged out")
            time.sleep(1)
            break
        else:
            print("Invalid input. Type Y/N")


def main():
    """
    Main function to call other functions in the program
    """
    app_banner()
    login_check()
    choose_level()
    restart_game()

main()
