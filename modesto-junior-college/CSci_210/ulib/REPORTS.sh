#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 07
# File: REPORTS.sh
#
# UNIX Library
# REPORTS: This program is the main driver for the REPORTS menu.
#          It shows the reports menu and invokes the appropriate
#          program according to the user selection.
#

error_flag=0 # initialize the error flag, indicating no error

while true; do # loop forever

	if [ $error_flag -eq 0 ]; then # check for the error

		tput clear
		tput cup 5 10
		echo "UNIX Library - ${BOLD}REPORTSMENU${NORMAL}"

		tput cup 7 20
		echo "0: ${BOLD}RETURNS{NORMAL} To The Main Menu"

		tput cup 9 20
		echo "1: Sorted by ${BOLD}TITLES ${NORMAL}"
		tput cup 11 20
		echo "2: Sorted by ${BOLD}AUTHOR ${NORMAL}"
		tput cup 13 20
		echo "3: Sorted by ${BOLD}CATEGORY ${NORMAL}"
	fi

	error_flag=0 # reset error flag

	tput cup 17 10
	echo "Enter your choice> _\b\c"
	read choice
	#
	#	case construct for checking the user selection
	#
	case $choice in
	0) exit 0 ;;
	1) REPORT_NO 1 ;;
	2) REPORT_NO 2 ;;
	3) REPORT_NO 3 ;;
	*)
		ERROR 20 10 # call ERROR program
		tput cup 20 1
		tput ed      # clear the rest of the screen
		error_flag=1 # set error flag to indicate error
		;;
	esac

done

exit 0
