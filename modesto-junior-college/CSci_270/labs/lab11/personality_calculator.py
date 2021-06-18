#!/usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 11
# Filename: personality_calculator.py
# Version: 1.5.0
#
# Description: A program which calculates a "unique personality type" from user
#              input.  The user provided birthdate information is run through
#              an algorithm which then outputs a "personality type", chinese
#              zodiac, and western zodiac for the user.  The program then
#              generates and displays the information graphical user
#              interface and webpage.  The program then stores the information
#              in a database and log file.
#

import webbrowser
import turtle
import math
import datetime
import sqlite3
import personality_type
import personal_webpage


turtle.bgcolor("#102129")
turtle.bgpic("assets/Final.gif")
turtle.setup(width=1280, height=800)
turtle.color("White")
turtle.penup()
turtle.goto(0, -150)


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


def get_zodiac(birthDay, birthMonth):
    if birthMonth == 1:
        sign = 10 if (birthDay < 20) else 11
    elif birthMonth == 2:
        sign = 11 if (birthDay < 19) else 12
    elif birthMonth == 3:
        sign = 12 if (birthDay < 21) else 1
    elif birthMonth == 4:
        sign = 1 if (birthDay < 20) else 2
    elif birthMonth == 5:
        sign = 2 if (birthDay < 21) else 3
    elif birthMonth == 6:
        sign = 3 if (birthDay < 21) else 4
    elif birthMonth == 7:
        sign = 4 if (birthDay < 23) else 5
    elif birthMonth == 8:
        sign = 5 if (birthDay < 23) else 6
    elif birthMonth == 9:
        sign = 6 if (birthDay < 23) else 7
    elif birthMonth == 10:
        sign = 7 if (birthDay < 23) else 8
    elif birthMonth == 11:
        sign = 8 if (birthDay < 22) else 9
    elif birthMonth == 12:
        sign = 9 if (birthDay < 22) else 10

    return sign


paragraph_number = int(birthMonth + birthDay + birthYear)

while paragraph_number > 9:
    paragraph_number = birth_total(paragraph_number)

zodiac_number = ((birthYear - 2000) % 12) + 1
astrology = get_zodiac(int(birthDay), int(birthMonth))

date_of_birth = datetime.date(int(birthYear), int(birthMonth), int(birthDay))
today = datetime.date.today()
days_alive = (today - date_of_birth).days

calc_physical = math.sin((2 * math.pi * days_alive) / 23) * 100
physical = int(round(calc_physical))

calc_emotional = math.sin((2 * math.pi * days_alive) / 28) * 100
emotional = int(round(calc_emotional))

calc_intellectual = math.sin((2 * math.pi * days_alive) / 33) * 100
intellectual = int(round(calc_intellectual))

results = (
    "Hi {}!".format(username)
    + personality_type.paragraph[paragraph_number]
    + "\n"
    + personality_type.chinese_zodiac[zodiac_number]
    + "\n"
    + personality_type.western_zodiac[astrology]
    + "\n"
    + "Physical: {} Emotional: {} Intellectual: {}".format(
        str(physical), str(emotional), str(intellectual)
    )
)

turtle.write(results, False, align="center", font=("Arial", 10, "bold"))
turtle.hideturtle()
turtle.done()


webpage_filename = "personality-calculator.html"
generate_webpage = open(webpage_filename, "w")
generate_webpage.write(
    personal_webpage.header
    + username
    + personal_webpage.personality
    + personality_type.paragraph[paragraph_number]
    + personal_webpage.bio_physical
    + str(physical)
    + personal_webpage.bio_emotion
    + str(emotional)
    + personal_webpage.bio_intellect
    + str(intellectual)
    + personal_webpage.zodiac_west
    + personality_type.western_zodiac[astrology]
    + personal_webpage.zodiac_china
    + personality_type.chinese_zodiac[zodiac_number]
    + personal_webpage.footer
)
generate_webpage.close()

webbrowser.open_new_tab(webpage_filename)


log_filename = "personality.log"
generate_log = open(log_filename, "a")
generate_log.write(
    "DOB: {}-{}-{}\n".format(str(birthMonth), str(birthDay), str(birthYear))
    + "Physical: {} Emotional: {} Intellectual: {}\n".format(
        str(physical), str(emotional), str(intellectual)
    )
    + personality_type.western_zodiac[astrology]
    + personality_type.chinese_zodiac[zodiac_number]
    + "\n"
    + personality_type.paragraph[paragraph_number]
    + "\n"
)
generate_log.close()


database_connect = sqlite3.connect("personality.sqlite")
database_cursor = database_connect.cursor()

birthdate = int(str(int(birthMonth)) + str(int(birthDay)) + str(int(birthYear)))


def create_table():
    sql_string = (
        "CREATE TABLE IF NOT EXISTS users (name text, birthdate "
        + "integer, paragraph_number integer, zodiac_number "
        + "integer, astrology integer, physical integer, emotional "
        + "integer, intellectual integer)"
    )

    database_cursor.execute(sql_string)
    database_connect.commit()


def insert_entry():
    sql_string = (
        "INSERT INTO users(name, birthdate, paragraph_number, "
        + "zodiac_number, astrology, physical, emotional, "
        + "intellectual) VALUES ('username', 'birthdate', "
        + "'paragraph_number', 'zodiac_number', 'astrology', "
        + "'physical', 'emotional', 'intellectual')"
    )

    database_cursor.execute(sql_string)
    database_connect.commit()


create_table()
insert_entry()
