#!/usr/bin/env Python3
#
# Author:  August Frisk
# Course:  CSci 270 - Fall 2017
# Assignment:  Lab 10
# Filename:  personal_webpage.py
# Version: 1.0.0
#
# Description: This file contains the contents and documentation to generate a
#              webpage for the program Personality Calculator.
#

# Doctype, opening html tag, and everyting within the head tag
header = """<!DOCTYPE html>
<html>
  <head>
    <title>Personality Calculator</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" />

    <!--  CSS to add character to the generated webpage  -->
    <style>

      * {
        margin: 0;
        padding: 0;
      }

      body {
        font-family: "Source Sans Pro", Helvetica, sans-serif;
        font-size: 13pt;
        padding: 10px;
        margin: 0;
        background-image: url("https://images.pexels.com/photos/816608/pexels-photo-816608.jpeg?cs=srgb&dl=pexels-alex-andrews-816608.jpg&fm=jpg");
        background-attachment: fixed;
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
      }

      h1 {
        font-size: 15pt;
        color: #636363;
        text-align: center;
        padding: 18px 0 18px 0;
        margin: 0 0 10px 0;
      }

      h1 span {
        border: 4px dashed #20bcd5;
        padding: 10px;
      }

      p {
        padding: 0;
        margin: 0;
      }

      .img-circle {
        border: 3px solid white;
        border-radius: 50%;
      }

      .section {
        background-color: #ffffff;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 10px;
      }

      #header {
        background-color: transparent;
      }

      #header img {
        display: block;
        width: 80px;
        height: 80px;
        margin: auto;
      }

      #header p {
        font-size: 25pt;
        color: #ffffff;
        padding-top: 5px;
        margin: 0;
        font-weight: bold;
        text-align: center;
      }

      .quote {
        font-size: 12pt;
        text-align: right;
        margin-top: 10px;
      }

      .copyright {
        font-size: 8pt;
        text-align: right;
        padding-bottom: 10px;
        color: #636363;
      }

    </style>
  </head>
"""

# Opening tags for body and header of the webpage. Header includes an icon and
# title of the webpage.
body = """
  <body>
  
    <div id="header" class="section">
      <img class="img-circle" src="https://www.iconexperience.com/_img/o_collection_png/green_dark_grey/512x512/plain/astronaut.png" alt="" />
      <p>Personality Calculator</p>
    </div>
"""

# Opening tag to main section of the webpage, and opening tag to the main
# heading. This is where the user's name is added to the webpage.
section_h1 = """
    <div class="section">
      <h1><span>"""

# Closing tags for the main heading. Opening for the main paragraph secton.
# This is where the user's unique personality paragraph is added to the webpage.
section_p = """</span></h1>
      <p>"""

# Closing tag for the main paragraph section. Opening tag for the quote section.
# This is where the user's chinese zodiac is added to the webpage.
section_quote = """</p>
      <p class="quote">"""

# Closing tag for the quote section. Copyright section for the footer. Closing
# tags for the main section, body, and html.
footer = """</p>
    </div>

    <div class="copyright">&copy; 2017 August Frisk. All rights reserved.</div>

  </body>
</html>
"""
