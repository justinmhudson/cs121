#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 05/04/2026

################################

import random

def valid(number_string):
    if number_string.isdecimal() and int(number_string) >= 0 and int(number_string) <= 10:
        return True
    else:
        return False

def plural_of_try(number):
    if number == 1:
        return "try"
    else:
        return "tries"

print("\n")

counter = 0
while True:
    while True:
        user_input = input("Guess any number from 1 to 10: ")
        if valid(user_input):
            break
        print("Invalid Entry. Please enter an integer between 0 and 10 inclusive.")

    random_number = random.randint(1,10)
    user_guess = int(user_input)

    print(f"\nYour Guess: {user_guess} \nRandom Number: {random_number}")

    if user_guess == random_number:
        counter += 1
        print("\nYou got it!")
        print(f"And it only took {counter} {plural_of_try(counter)}!\n")
        break
    elif user_guess < random_number:
        counter += 1
        print("\nToo low!\n")
    else:
        counter += 1
        print("\nToo high!\n")


get_ipython().system('jupyter nbconvert --to script --no-prompt --TagRemovePreprocessor.remove_cell_tags="[\'remove\']" Assignment_3_4.ipynb')

