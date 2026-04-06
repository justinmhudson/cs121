#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 05/04/2026

################################

import random

def int_to_word(number):
    match number:
        case 1:
            result = "Heads"
        case 2:
            result = "Tails"
        case _:
            result = "Error"
    return result

print("\n")
user_guess = None
while user_guess != 0:
    while True:
        user_input = input("Guess Heads(1) OR Tails(2) OR Exit(0). Enter 1/2/0: ")
        if user_input == "0" or user_input == "1" or user_input == "2":
            break
        print("Invalid Entry. Please enter 1 (Heads), 2 (Tails) or 0 (Exit)")

    coin_flip = random.randint(1,2)
    user_guess = int(user_input)

    if user_guess != 0:
        print(f"\nYour Guess: {int_to_word(user_guess)} \nCoin: {int_to_word(coin_flip)}")

    if user_guess == 0:
        print("\nGoodbye!\n")
    elif coin_flip == user_guess:
        print("\nYou win!\n")
    else:
        print("\nYou lose...\n")

