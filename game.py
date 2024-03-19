# imports from python library
import time


def level_banner():
    """
    function to display difficulty level for a user to select
    """
    print("Choose a level from below...\n")
    print("Select Easy or Advanced \n")
    print("Please type in E to play 'Easy Level' or A to play 'Advanced Leve'\n")

def choose_level():
    """
    function to accept user input for difficulty level
    """
    while True:

        user_input = input("Please input E or A to select a level...")
        if user_input.lower() == 'e':
            print("This is Easy Level\n")
            play_guess_advanced()
            break
        if user_input.lower() == 'a':
            print("This is Advanced Level") 
            play_guess_advanced()
            break
        else:
            print("Please type in E or A to select a level")


def select_random_word():
    """
    Select random word from list words and return in upper case
    """
    random_word = random.choice(countries)
    return random_word.upper()


def play_guess_advanced(random_word):
    """
    Function for the game which inherit randomWord from randomWord function
    and run a while loop until no tries left. The function displays the game
    as the loop runs and validates if inputs by user is wrong and prompt
    users of the errors
    """
    guessed_letters = countries

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
            print("OOO! You lost this time!!! Better luck next time :)\n")
            print (f"The correct word is {random_word}.\n")

    return tries

