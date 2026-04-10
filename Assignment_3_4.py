#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 09/04/2026

################################

# Import library for randint function
import random

# Function to validate user input
def validate(number_string):
    if number_string.isdecimal() and int(number_string) >= 1 and int(number_string) <= 10:
        return True
    else:
        return False

# Variable to keep track of attempts
number_of_tries = 0

# Generate random number
random_number = random.randint(1,10)

# Loop until user guesses correctly
print("\n")
while True:
    # Collect and validate user input
    while True:
        user_input = input("Guess any number from 1 to 10: ")
        if validate(user_input):
            break
        print("Invalid Entry. Please enter an integer between 1 and 10 inclusive.\n")

    # Increment counter and compare guess to random number
    number_of_tries += 1
    user_guess = int(user_input)
    if user_guess == random_number:
        print("You got it!")
        print(f"And it only took {number_of_tries} tr{'y' if number_of_tries == 1 else 'ies'}!\n")
        break
    elif user_guess < random_number:
        print("Too low!\n")
    else:
        print("Too high!\n")

