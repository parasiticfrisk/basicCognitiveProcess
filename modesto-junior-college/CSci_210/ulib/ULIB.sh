#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 01
# File: ULIB.sh
#
# UNIX Library
# ULIB: This program is the main driver for the UNIX library application
#       program. It shows a brief startup message and the displays the
#       main menu.
#       It invokes the appropriate program according to the user selection.
#

BOLD=$(tput smso)
NORMAL=$(tput rmso)
export BOLD NORMAL
#
#  show the title and a brief message before showing the main menu
#
tput clear
tput cup 5 15
echo "${BOLD}Super Duper UNIX Library"
tput cup 12 10
echo "${NORMAL}This is the UNIX Library application"
tput cup 14 10
echo "Please enter any key to continue..._\b\c"
read answer

error_flag=0 # initialize the error flag, indicating no error

while true; do # loop forever

	if [ $error_flag -eq 0 ]; then # check for the error

		tput clear
		tput cup 5 10
		echo "UNIX Library - ${BOLD}MAIN MENU${NORMAL}"
		tput cup 7 20
		echo "0: ${BOLD}EXIT${NORMAL} this program"
		tput cup 9 20
		echo "1: ${BOLD}EDIT${NORMAL} Menu"
		tput cup 11 20
		echo "2: ${BOLD}REPORTS${NORMAL} Menu"

		error_flag=0 # reset error flag
	fi

	tput cup 13 10
	echo "Enter your choice> _\b\c"
	read choice
	#
	#	case construct for checking the user selection
	#
	case $choice in
	0)
		tput clear
		exit 0
		;;
	1) EDIT ;;
	2) REPORTS ;;
	*)
		ERROR 20 10 # call ERROR program
		tput cup 20 1
		tput ed      # clear the rest of the screen
		error_flag=1 # set error flag to indicate error
		;;
	esac

done

exit 0
