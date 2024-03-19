# imports from python library
import random
import time
import os


#internal imports from exiting python file
from authenticator import login
from authenticator import signup
from authenticator import login_data
from game import level_banner
from game import choose_level
from game import play_guess_advanced

# A list of countries to be chosen at random
countries = ['England', 'Ghana', 'America', 'Nigeria',
             'Italy', 'China', 'Mali', 'Russia',
             'Argentina', 'Jamaica', 'Canada',
            'Brazil', 'Egypt', 'Norway']


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

# def select_random_word():
#     """
#     Select random word from list words and return in upper case
#     """
#     random_word = random.choice(countries)
#     return random_word.upper()


# def play_guess_country(random_word):
#     """
#     Function for the game which inherit randomWord from randomWord function
#     and run a while loop until no tries left. The function displays the game
#     as the loop runs and validates if inputs by user is wrong and prompt
#     users of the errors
#     """
#     guessed_letters = countries

#     tries = 10
#     print(f"Total Attempts: {tries}\n")
#     print(" _ " * len(random_word))

#     while tries > 0:
#         wrong_letter_count = 0
#         guess = input(" Please enter your guess: ").upper()

#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print(f"{guess} is already guessed!")
#                 print(f"\n Attempt left: {tries}\n")
#             elif guess not in random_word:
#                 print("\n You guessed wrong. Try Again")
#                 tries -= 1
#                 guessed_letters += guess
#                 print(f"\n Attempt left: {tries}\n")
#             else:
#                 print(f"\n Correct! {guess} is in the word.")
#                 print(f"\n Attempt left: {tries}\n")
#         else:
#             print("\n Invalid input. Enter only one alphabet")
#             print(f"\n Attempt left: {tries}\n")
#         guessed_letters += guess

#         for letter in random_word:
#             if letter in guessed_letters:
#                 print(f"{letter}", end=' ')
#             else:
#                 print(" _ ", end=' ')
#                 wrong_letter_count += 1

#         if wrong_letter_count == 0:
#             print(f"\nCongrats. The secret word is {random_word}.")
#             print("\nHURAAYYY!!! You Guessed correctly :)")
#             break
#         if tries == 0:
#             print("\n")
#             print("OOO! You lost this time!!! Better luck next time :)\n")
#             print (f"The correct word is {random_word}.\n")

#     return tries


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
    # play_guess_country(select_random_word())
    restart_game()

main()
