#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 03
# Filename: coin_calculator.py
#
# Description: A program that collects input from the user and calculates the
#              toatl currency.  The user provides a total number of each U.S.
#              coin type, and the program then calculates and dislpays the
#              results to the user.
#

print("Welcome to the Computer Science 270 Coin Calculator.")
print("You tell us how many, we'll tell you how much!")

print("For the following, enter only integer values")

quarters = int(input("Enter number of quarters: "))
dimes = int(input("Enter number of dimes: "))
nickels = int(input("Enter number of nickels: "))
pennies = int(input("Enter number of pennies: "))

total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies

dollars = total_cents // 100
cents = total_cents % 100

print("You have a total of ${}.{}".format(dollars, cents))
