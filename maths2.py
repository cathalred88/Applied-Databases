# maths.py
# Code for running maths flashcard game
# Author John Elder, Transcribed by Cathal Redmond 27-May-2025

#imports
import os
import random


#define constants 
clear = lambda: os.system('cls')

# Start game function
# function To Start The Game And Pick Cards
def start_game():               
    clear()             #clear the screen
    print("Welcome to Math Flashcards!")
    pick = input(
        "Choose your flashcards (add|subtract|multiply|divide): ")

    if pick.lower() == "a":
        print(f"You picked {pick}")
        add_flashcards()
    elif pick.lower() == "s":
        print(f"You picked {pick}")
        subtract_flashcards()
    elif pick.lower() == "m":
        print(f"You picked {pick}")
        multiply_flashcards()
    elif pick.lower() == "d":
        print(f"You picked {pick}")
        divide_flashcards()
    else:
        print(f"Sorry, I don't recognize {pick}")
        input("Please hit enter to try again")
        start_game()



# Start Addition Flashcards Function
def add_flashcards():
    clear()
    card_one = random.randint(0,10)
    card_two = random.randint(0,10)
    correct = card_one + card_two
    answer = input(f"{card_one} + {card_two}: ")

    if int(answer) == correct:
        print(f"Correct! {card_one} + {card_two} = {answer}")
    else:
        print(f"Wrong! {card_one} + {card_two} = {correct}")
    play = input("Would you like another card? (yes|no|restart): ")

    if play.lower() == "y":
        add_flashcards()
    elif play.lower() == "n":
        print("Thanks for playing!")
    elif play.lower() == "r":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        add_flashcards()
# End Addition Flashcards Function

# Start Subtraction Flashcards Function
def subtract_flashcards():
    clear()
    card_one = random.randint(0,10)
    card_two = random.randint(0,10)
    correct = card_one - card_two
    answer = input(f"{card_one} - {card_two}: ")

    if int(answer) == correct:
        print(f"Correct! {card_one} - {card_two} = {answer}")
    else:
        print(f"Wrong! {card_one} - {card_two} = {correct}")
    play = input("Would you like another card? (yes|no|restart): ")

    if play.lower() == "y":
        subtract_flashcards()
    elif play.lower() == "n":
        print("Thanks for playing!")
    elif play.lower() == "r":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        subtract_flashcards()
# End Subtraction Flashcards Function

# Start Multiply Flashcards Function
def multiply_flashcards():
    clear()
    card_one = random.randint(0,10)
    card_two = random.randint(0,10)
    correct = card_one * card_two
    answer = input(f"{card_one} x {card_two}: ")

    if int(answer) == correct:
        print(f"Correct! {card_one} x {card_two} = {answer}")
    else:
        print(f"Wrong! {card_one} x {card_two} = {correct}")
    play = input("Would you like another card? (yes|no|restart): ")

    if play.lower() == "y":
        multiply_flashcards()
    elif play.lower() == "n":
        print("Thanks for playing!")
    elif play.lower() == "r":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        multiply_flashcards()
# End multiply Flashcards Function


# Start Division Flashcards Function
def divide_flashcards():
    clear()
    card_one = random.randint(0,10)
    card_two = random.randint(1,10)
    correct = card_one / card_two
    answer = input(f"{card_one} / {card_two}: ")

    if int(answer) == correct:
        print(f"Correct! {card_one} / {card_two} = {answer}")
    else:
        print(f"Wrong! {card_one} / {card_two} = {correct}")
    play = input("Would you like another card? (yes|no|restart): ")

    if play.lower() == "y":
        divide_flashcards()
    elif play.lower() == "n":
        print("Thanks for playing!")
    elif play.lower() == "r":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        divide_flashcards()
# End division Flashcards Function

start_game()