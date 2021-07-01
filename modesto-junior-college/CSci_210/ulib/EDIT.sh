#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 02
# File: EDIT.sh
#
# UNIX Library
# EDIT: This program is the main driver for the EDIT program.
#       It shows the EDIT menu and invokes the appropriate program
#       according to the user selection.
#

error_flag=0 # initialize the error flag indicating no error

while true; do # loop forever

	if [ $error_flag -eq 0 ]; then # check for the error

		tput clear
		tpup cut 5 10
		echo "UNIX Library - ${BOLD}EDITMENU${NORMAL}"
		tput cup 7 20
		echo "0: ${BOLD}RETURN${NORMAL}To the Main Menu"
		tput cup 9 20
		echo "1:${BOLD}ADD${NORMAL}"
		tput cup 11 20
		echo "2:${BOLD}UPDATESTATUS${NORMAL}"
		tput cup 13 20
		echo "3:${BOLD}DISPLAY${NORMAL}"
		tput cup 15 20
		echo "4:${BOLD}DELETE${NORMAL}"
	fi

	error_flag=0 # reset error flag

	tput cup 17 20
	echo "Enter your choice>_\b\c"
	read choice
	#
	#	case construct for checking user selection
	#
	case $choice in
	0) exit 0 ;;
	1) ADD ;;
	2) UPDATE ;;
	3) DISPLAY ;;
	4) DELETE ;;
	*)
		ERROR 20 10 # call ERROR program
		tput cup 20 1
		tput ed # clear the rest of the screen
		error_flag=1
		;; # set error flag to indicate
	esac

done

exit 0
