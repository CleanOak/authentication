
import random
import time
import os

# from authenticator import login
# from authenticator import signup
from authenticate import login_data


countries = ['England', 'Ghana', 'America', 'Nigeria',
             'Italy', 'China', 'Mali', 'Russia',
             'Argentina', 'Jamaica', 'Canada',
            'Brazil', 'Egypt', 'Norway']



def game_banner():
    """
    function to display banner for the game
    """
    print("++++++++++++++++++++++++++++++++++++")
    print("*** WELCOME TO THE GUESSING GAME ***")
    print("++++++++++++++++++++++++++++++++++++\n")


def login_check():
    """
    Ask user if they have login credentials or not
    """
 
    userAnswer  = input("Do you already have an account? y/n\n")
    if userAnswer.lower() == 'y':
        return 1
    elif userAnswer.lower() == 'n':
        return 0
    else:
         print ("Please enter y or n")

   

    



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
        guess = input(f" Please enter your guess: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{guess} is already guessed!")
                
                print(f"\n Attempt left: {tries}\n")
            elif guess not in random_word:
                print(f"\n You guessed wrong. Try Again")
                tries -= 1
                guessed_letters += guess
                
                print(f"\n Attempt left: {tries}\n")
            else:
                print(f"\n Correct! {guess} is in the word.")
                
                print(f"\n Attempt left: {tries}\n")
        else:
            print(f"\n Invalid input. Enter only one alphabet")
            
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
            print("\nYou Guessed correctly:)")
            break
        if tries == 0:
            print("\n")
            print(f"OOO! You lost this time but better luck next time :)\n The correct word is {random_word}.\n")

    return tries


def restart_game():
    """
    Function to ask user if they want to play again
    and restart the game and if not exit the terminal
    """
    while True:
        answer = input(f"\nDo you want to play again?: Y/N\n")
        os.system('clear')
        if answer.upper() == "Y":
            print(f"\nTRY YOUR LUCK AGAIN!!")
            print(f"\nRestarting Game......")
            time.sleep(2.5)
            play_guess_country(select_random_word())
        elif answer.upper() == "N":
            time.sleep(1.5)
            print(f"\nGood Bye!!")
            time.sleep(1.5)
            print(f"\nLogging Out....")
            time.sleep(3)
            break
        else:
            print(f"Invalid input. Type Y/N")


def main():
    game_banner()
    login_check()


    #play_guess_country(select_random_word())
    #restart_game()


main()