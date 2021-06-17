#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 09
# Filename: personality_calculator.py
# Version: 1.3.0
#
# Description: A program which calculates a "unique personality type" from user
#              input.  The user provided birthdate information is run through
#              an algorithm which then outputs a "personality type" and
#              chinese zodiac for the user.  The program then generates and
#              displays the information in a webpage, and stores the
#              information in a log file.
#

import webbrowser
import personality_type
import personal_webpage

print("Welcome to the Computer Science 270 Personality Calculator")
print("Let's find out what makes you special!")

username = input("Please enter your name: ")

print("For the following, please enter only integer values")

birthMonth = int(input("Please enter your birth month: "))
birthDay = int(input("Please enter your birth day: "))
birthYear = int(input("Please enter your birth year: "))

birth_sum = birthMonth + birthDay + birthYear

paragraph_number = birth_sum % 9

if paragraph_number == 0:
    paragraph_number = 9

zodiac_number = ((birthYear - 2000) % 12) + 1

print(
    "\n"
    + "Hi {}! You were born in the year of the ".format(username)
    + personality_type.chinese_zodiac[zodiac_number]
    + personality_type.paragraph[paragraph_number]
)
print("Now you know what makes you special!")
print(
    "\n"
    + "generating webpage...\n"
    + "generating log file...\n"
    + "opening genereated webpage.."
)

webpage_filename = "personality-calculator.html"
generate_webpage = open(webpage_filename, "w")
generate_webpage.write(
    personal_webpage.header
    + personal_webpage.body
    + personal_webpage.section_h1
    + username
    + personal_webpage.section_p
    + personality_type.paragraph[paragraph_number]
    + personal_webpage.section_quote
    + personality_type.chinese_zodiac[zodiac_number]
    + personal_webpage.footer
)
generate_webpage.close()

log_filename = "personality.log"
generate_log = open(log_filename, "a")
generate_log.write(
    "DOB: {}-{}-{}\n".format(str(birthMonth), str(birthDay), str(birthYear))
    + "Paragraph number: {}\n".format(str(paragraph_number))
    + "Zodiac number: {}\n".format(str(zodiac_number))
)
generate_log.close()

webbrowser.open_new_tab(webpage_filename)
