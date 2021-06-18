#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 02
# Filename: birth_sum.py
#
# Description: A program that provides a "unique" output based on user input.
#              The "unique" output is the sum of the user's provided birthdate.
#

print("Welcome to the Computer Science 270 Birthdate Calculator.")
print("Let's calculate what makes you special!")

name = input("What is your name? ")

print("For the following, enter only integer values")

birthMonth = int(input("What month were you born? "))
birthDay = int(input("What day of the month were you born? "))
birthYear = int(input("What is your birth year? "))

birth_sum = birthMonth + birthDay + birthYear

print("Hello " + name + ", your special birth sum adds up to be " + str(birth_sum))
