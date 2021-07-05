#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignmen: Lab 10
# Filename: personality_calculator.py
# Version: 1.4.0
#
# Description: A program which calculates a "unique personality type" from user
#              input.  The user provided birthdate information is run through
#              an algorithm which then outputs a "personality type" and
#              chinese zociac for the user.  The program then generates and
#              displays the information in a webpage, then stores the
#              information in a log file.
#

import webbrowser
import turtle
import personality_type
import personal_webpage

username = turtle.textinput("Name", "Please enter your name")
birthMonth = turtle.numinput(
    "Month of birth", "Enter your birth month", 1, minval=1, maxval=12
)
birthDay = turtle.numinput(
    "Day of birth", "Enter your birth day", 1, minval=1, maxval=31
)
birthYear = turtle.numinput(
    "Year of birth", "Enter your birth year", 1997, minval=1900, maxval=2020
)


def birth_total(paragraph_number):
    return sum([int(x) for x in str(paragraph_number)])


paragraph_number = int(birthMonth) + int(birthDay) + int(birthYear)

while paragraph_number > 9:
    paragraph_number = birth_total(paragraph_number)

zodiac_number = ((birthYear - 2000) % 12) + 1

results = (
    "Hi {}! You were born in the year of the ".format(username)
    + personality_type.chinese_zodiac[zodiac_number]
    + personality_type.paragraph[paragraph_number]
)

turtle.write(results, False, align="center", font=("Arial", 12, "bold"))

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
