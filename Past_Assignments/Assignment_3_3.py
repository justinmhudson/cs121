#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 07/04/2026

################################

import random

print("\n")
while True:
    while True:
        user_input = input("Guess Heads(1) OR Tails(2), or Exit(0). Enter 1/2/0: ")
        if user_input == "0" or user_input == "1" or user_input == "2":
            break
        print("Invalid Entry. Please enter 1 (Heads), 2 (Tails) or 0 (Exit)\n")

    if user_input == "0":
        print("Goodbye!\n")
        break
    else:
        coin_flip = random.randint(1,2)
        user_guess = int(user_input)
        if coin_flip == user_guess:
            print("You win!\n")
        else:
            print("You lose...\n")

