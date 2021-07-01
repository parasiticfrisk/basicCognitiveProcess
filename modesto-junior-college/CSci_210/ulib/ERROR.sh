#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 09
# File: ERROR.sh
#
# UNIX Library
# ERROR: This program displays an error message and waits for user
#	     input to continue. It displays the message at the specified
#	     row and column.
#

tput cup $1 $2                            # place the cursor on the screen
echo "Wrong Input. Try again."            # show the error message
echo "Press any key to continue...>_\b\c" # display the prompt
read answer                               # read user input
exit 0                                    # indicate normal exit
