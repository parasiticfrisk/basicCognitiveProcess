#!/usr/bin/env Python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 11
# Filename: personal_webpage.py
# Version: 2.0.0
#
# Description: This file contains the contents and documentation to generate a
#              webpage for the program Personality Calculator.
#

# Doctype, opening html tag, and everyting within the head tag, opening tags for
# body, wrapper, & heading. This is where user's name is added to webpage.
header = """<!DOCTYPE HTML>
<!--
    August Frisk
    CSci 270 - Fall 2017
    Lab 11
    Personality Calculator
    (c) 2017 MIT License
-->
<html lang="en-US">

<head>
    <title>Personality Calculator</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/main.css" />

</head>

<body class="is-preload">

    <!-- Wrapper -->
    <div id="wrapper">

        <!-- Header -->
        <header id="header" class="alt">
            <span class="logo"><img src="https://flaticons.net/icon.php?slug_category=brand-identity&slug_icon=readernaut" alt="" /></span>
            <h1>"""

# Closing tag for header h1, & header tag. Start of main div, start of
# personality section. This is where the personality paragraph is added to the
# webpage.
personality = """</h1>
            <p>Here is what makes you special!</p>
        </header>

        <!-- Main -->
        <div id="main">

            <!-- Personality Type -->
            <section class="main">
                <div class="personality">
                    <div class="content">
                        <header class="major">
                            <h2>Personality Type</h2>
                        </header>
                        <p>"""

# Closing tags for personality section. Start of the bio-rhythm section. This is
# where the physical results are added to the webpage.
bio_physical = """</p>
                    </div>
                    <span class="image"><img src="https://images.pexels.com/photos/3078831/pexels-photo-3078831.jpeg?cs=srgb&dl=pexels-nadi-lindsay-3078831.jpg&fm=jpg" alt="" /></span>
                </div>
            </section>

            <!-- Bio-Rhythm -->
            <section class="main special">
                <header class="major">
                    <h2>Bio-Rhythm</h2>
                </header>
                <ul class="bio-rhythm">
                    <li>
                        <span class="icon solid major style1 fa-running"></span>
                        <h3>Physical</h3>
                        <p>"""

# This is where the emotional results are added to the webpage.
bio_emotion = """</p>
                    </li>
                    <li>
                        <span class="icon solid major style2 fa-theater-masks"></span>
                        <h3>Emotional</h3>
                        <p>"""

# This is where the intellectual results are added to the webpage.
bio_intellect = """</p>
                    </li>
                    <li>
                        <span class="icon solid major style3 fa-book-reader"></span>
                        <h3>Intellectual</h3>
                        <p>"""

# Closing tags for the bio-rhythm section. Start of the zodiac section. This is
# where the western astrology results are added to the webpage.
zodiac_west = """</p>
                    </li>
                </ul>
            </section>

            <!-- Zodiac -->
            <section class="main special">
                <header class="major">
                    <h2>Zodiac</h2>
                    <p>"""

# This is where the chinese zodiac results are added to the webpage.
zodiac_china = """</p>
                    <p>"""

# Closing tags for the zodiac section, main div, wrapper, body, & html. Footer
# section includes copyright and authorship.
footer = """                    </p>
                </header>
            </section>

        </div>

        <!-- Footer -->
        <footer id="footer">
            <p class="copyright">&copy; 2017 August Frisk. Created with <i class="fab fa-python"></i> <i class="fab fa-html5"></i> <i class="fab fa-css3-alt"></i>.</p>
        </footer>

    </div>

</body>

</html>
"""
