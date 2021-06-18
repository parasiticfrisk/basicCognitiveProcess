#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Asignment: Lab 01
# Filename: guessing_game.py
#
# Original Author: Professor Dale Phillips
# Author URL: https://github.com/phillipsd
#
# Description: A number guessing game in which the player attempts to guess
#              a randomly generated integer within a set amount of tries.  The
#              program provides feedback based on the player's guess, letting
#              them know if it is too high, too low, or correct.  The player
#              wins if they guess correctly, and loses if they run out of
#              guess attempts.
#

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0
maxAttempts = 6

print("AHOY! I'm the Dreaded Petey the Pirate, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries. ")


while guess != secret and attempts < maxAttempts:

    guess = int(input("What's yer guess? "))

    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")

    attempts = attempts + 1


if guess == secret:
    print("Avast! Ye got it! Found my secret ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was ", secret)
