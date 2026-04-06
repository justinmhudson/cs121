#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 13/03/2026

################################

# import statistsics to access mean(), multimode(), and median()

import statistics

################################

# Functions to use in main code

## Converts cardinal number to ordinal number for user prompt
def ordinal(number):
   cardinal_string = str(number)   
   if cardinal_string.endswith("11") or cardinal_string.endswith("12") or cardinal_string.endswith("13"):
       return cardinal_string + "th"
   elif cardinal_string.endswith("1"):
       return cardinal_string + "st"
   elif cardinal_string.endswith("2"):
       return cardinal_string + "nd"
   elif cardinal_string.endswith("3"):
       return cardinal_string + "rd"
   else:
       return cardinal_string + "th"

## Checks if user input is a number (positive or negative, int or floating point)
def is_number(number_string):
    try:
        float(number_string)
        return True
    except ValueError:
        return False

## Checks if user input is a positive integer
def is_positive_integer(number_string):
    if number_string.isdecimal() and int(number_string) > 0:
        return True
    else:
        return False

## Prints list of numbers horizontally, separated by commas
def print_horizontal(list_):
    last_index = len(list_) - 1
    for index, item in enumerate(list_):
        if index == last_index:
            print(f"{item:g}")
        else:
            print(f"{item:g}, ", end="")

################################

# Section 1: Writing Code for Sum, Max, Min, Average

## User inputs size of list (Validates input is positive integer)
print("\n")
while True:
    user_input = input("How many numbers would you like to calculate? ")
    if is_positive_integer(user_input):
        break
    print("Please try again. You may only enter a positive integer.")

## User inputs each element of list (Validates each input is a valid number)
list_size = int(user_input)
list_of_numbers = []
i = 0
while i < list_size:
    next_number = input(f"Input the {ordinal(i + 1)} number: ")
    if is_number(next_number):
        list_of_numbers.append(float(next_number))
        i += 1
    else:
        print("Please try again. You may only enter integers or floating-point numbers.")

## Print list of numbers horizontally (separated by commas)
print("\nList of Numbers (Horizontal):")
print_horizontal(list_of_numbers)

## Print list of numbers vertically
print("\nList of Numbers (Vertical):")
for number in list_of_numbers:
    print(f"{number:g}")

## Calculate sum, max, min and average of list using code
list_sum = 0
list_max = list_of_numbers[0]
list_min = list_of_numbers[0]
for number in list_of_numbers:
    list_sum += number
    if number > list_max:
        list_max = number
    if number < list_min:
        list_min = number        
list_avg = list_sum / list_size

## Calculate median of list using code
list_of_numbers.sort()
if list_size % 2 != 0:
    list_median = list_of_numbers[list_size // 2]
else:
    list_median = (list_of_numbers[list_size // 2] + list_of_numbers[(list_size // 2) - 1]) / 2

## Calculate mode of list using code
list_dictionary = {}
for number in list_of_numbers:
    count = list_dictionary.get(str(number), 0)
    list_dictionary.update({str(number): count + 1})

max_count = list(list_dictionary.values())[0]
for value in list_dictionary.values():
    if value > max_count:
        max_count = value

list_mode = []
for key in list_dictionary:
    if list_dictionary[key] == max_count:
        list_mode.append(float(key))

## Display them each with a corresponding label at the bottom
print("\nCustom Functions:")
print(f"Sum: {list_sum:g}")
print(f"Max: {list_max:g}")
print(f"Min: {list_min:g}")
print(f"Average: {list_avg:g}")
print(f"Median: {list_median:g}")
print("Mode: ", end="")
print_horizontal(list_mode)

################################

# Section 2: Use Python built-in functions to calculate sum, max, min and average

print("\nBuilt-In Functions:")
print(f"Sum: {sum(list_of_numbers):g}")
print(f"Max: {max(list_of_numbers):g}")
print(f"Min: {min(list_of_numbers):g}")
print(f"Average: {statistics.mean(list_of_numbers):g}")
print(f"Median: {statistics.median(list_of_numbers):g}")
print("Mode: ", end="")
print_horizontal(statistics.multimode(list_of_numbers))
print("\n")

