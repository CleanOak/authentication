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
            print("This is Easy Level")
            break
        if user_input.lower() == 'a':
            print("This is Advanced Level") 
            break
        else:
            print("Please type in E or A to select a level")

