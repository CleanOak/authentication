
import random
import time
import os



from authenticator import login
from authenticator import signup
from authenticator import login_data


countries = ['England', 'Ghana', 'America', 'Nigeria',
             'Italy', 'China', 'Mali', 'Russia',
             'Argentina', 'Jamaica', 'Canada',
            'Brazil', 'Egypt', 'Norway']


def app_banner():
    """
    function to display banner for the game for the application
    """
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("*** WELCOME TO THE WORLD GUESSING GAME ***")
    print("+++++++++++++++++++++++++++++++++++++++++++\n")

def game_banner():
    """
    Function to display the game and rules
    """
    print("++++++++++++++++++++++++++++++++++++")
    print("*** BRING ON YOUR BEST***")
    print("++++++++++++++++++++++++++++++++++++\n")


def login_check():
    """
    Ask user if they have login credentials or not
    """
    while True:

        user_answer  = input("Do you already have an account? y/n\n")
        if user_answer.lower() == 'y':
            user_exist()
        if user_answer.lower() == 'n':
            new_user()
            break
        else:
            print ("Please enter y or n")


def user_exist():
    """
    Checks if user already has login details
    """
    login(login_data())
    game_banner()


def new_user():
    """
    Allows new user to create username and password
    """
    signup()
    login(login_data())
    game_banner()

def select_random_word():
    """
    Select random word from list words and return in upper case
    """
    random_word = random.choice(countries)
    return random_word.upper()


def play_guess_country(random_word):
    """
    Function for the game which inherit randomWord from randomWord function
    and run a while loop until no tries left. The function displays the game
    as the loop runs and validates if inputs by user is wrong and prompt
    users of the errors
    """
    guessed_letters = "AEIOU"
    tries = 10
    print(f"Total Attempts: {tries}\n")
    print(" _ " * len(random_word))

    while tries > 0:
        wrong_letter_count = 0
        guess = input(" Please enter your guess: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{guess} is already guessed!")
                print(f"\n Attempt left: {tries}\n")
            elif guess not in random_word:
                print("\n You guessed wrong. Try Again")
                tries -= 1
                guessed_letters += guess
                print(f"\n Attempt left: {tries}\n")
            else:
                print(f"\n Correct! {guess} is in the word.")
                print(f"\n Attempt left: {tries}\n")
        else:
            print("\n Invalid input. Enter only one alphabet")
            print(f"\n Attempt left: {tries}\n")
        guessed_letters += guess

        for letter in random_word:
            if letter in guessed_letters:
                print(f"{letter}", end=' ')
            else:
                print(" _ ", end=' ')
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(f"\nCongrats. The secret word is {random_word}.")
            print("\nHURAAYYY!!! You Guessed correctly :)")
            break
        if tries == 0:
            print("\n")
            print("OOO! You lost this time but better luck next time :)\n")
            print (f"The correct word is {random_word}.\n")

    return tries


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
            time.sleep(2.5)
            play_guess_country(select_random_word())
        elif answer.upper() == "N":
            time.sleep(1.5)
            print("\nGood Bye!!")
            time.sleep(1.5)
            print("\nLogging Out....")
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
    play_guess_country(select_random_word())
    restart_game()

main()
