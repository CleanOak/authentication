
import random






countries = ['Englnd', 'Ghana', 'America', 'Nigeria',
             'Italy', 'China', 'Mali', 'Russia',
             'Argentina', 'Jamaica', 'Canada',
            'Brazil', 'Egypt', 'Norway']


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
    #print(Fore.WHITE + display_hangman(tries))
    print(f"Total Attempts: {tries}\n")
    print(" _ " * len(random_word))

    while tries > 0:
        wrong_letter_count = 0
        guess = input(f" Please enter your guess: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{guess} is already guessed!")
                #print(play_guess_country(tries))
                print(f"\n Attempt left: {tries}\n")
            elif guess not in random_word:
                print(f"\n You guessed wrong. Try Again")
                tries -= 1
                guessed_letters += guess
                #print(play_guess_country(tries))
                print(f"\n Attempt left: {tries}\n")
            else:
                print(f"\n Correct! {guess} is in the word.")
                #print(play_guess_country(tries))
                print(f"\n Attempt left: {tries}\n")
        else:
            print(f"\n Invalid input. Enter only one alphabet")
            #print(play_guess_country(tries))
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
            print("\nYou saved the man:)")
            break
        if tries == 0:
            print("\n")
            print(f"LOSER! The secret word was {random_word}.\n")

    return tries



play_guess_country(select_random_word())