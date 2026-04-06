#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 05/04/2026

################################

import random

def validate(number_string):
    if number_string.isdecimal() and int(number_string) >= 1 and int(number_string) <= 10:
        return True
    else:
        return False

counter = 0
random_number = random.randint(1,10)

print("\n")
while True:
    while True:
        user_input = input("Guess any number from 1 to 10: ")
        if validate(user_input):
            break
        print("Invalid Entry. Please enter an integer between 1 and 10 inclusive.")

    counter += 1
    user_guess = int(user_input)

    if user_guess == random_number:
        print("You got it!")
        print(f"And it only took {counter} tr{'y' if counter == 1 else 'ies'}!\n")
        break
    elif user_guess < random_number:
        print("Too low!\n")
    else:
        print("Too high!\n")

