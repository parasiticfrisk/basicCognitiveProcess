#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 05
# File: UPDATE.sh
#
# UNIX Library
# UPDATE: This program updates the status of a specific book. It asks the
#	      Author/Title of the book, and changes the status of the specified
#	      book from in (checked in) to out (checked out), or from out to in.
#	      If the book is no found in the file, an error message is displayed.
#

OLD_IFS="$IFS" # save the IFS settings

answer=y # initialize the answer to indicate yes
while [ "$answer" = y ]; do

	# declare empty variables
	new_status=
	new_bname=
	new_date=

	tput clear
	tput clear

	tput cup 3 5
	echo "Enter the Author/Title >_\b\c"
	read response
	grep -i "$response" ULIB_FILE >TEMP # find the specified book

	if [ -s TEMP ]; then # if it is found

		IFS=":" # set the IFS to colon
		read title author category status bname date <TTEMP
		tput cup 5 10
		echo "UNIX Library - ${BOLD}UPDATESTATUSMODE${NORMAL}"
		tput cup 7 23
		echo "Title: $title"
		tput cup 8 22
		echo "Author: $author"

		case $category in
		[Tt][Bb]) word=textbook ;;
		[Ss][Yy][Ss]) word=system ;;
		[Rr][Ee][Ff]) word=reference ;;
		*) word=undefined ;;
		esac

		tput cup 9 20
		echo "Category: $word"
		tput cup 10 22
		echo "Status: $status"

		if [ "$status" = "in" ]; then

			new_status=out # indicate the new status

			tput cup 11 18
			echo "New status: $new_status"
			tput cup 12 14
			echo "Checked out by: _\b\c"
			read new_bname

			new_date=$(date +%D)
			tput cup 13 24
			echo "Date: $new_date"

		else
			new_status=in
			tput cup 11 14
			echo "Checked out by: $bname"
			tput cup 12 24
			echo "Date: $date"
			tput cup 15 18
			echo "New status: $new_status"
		fi

		grep -iv "$title:$author:$category:$status:$bname:$date" ULIB_FILE >TEMP

		cp TEMP ULIB_FILE

		echo "$title:$author:$category:$new_status:$new_bname:$new_date" >>ULIB_FILE

	else # if book not found
		tput cup 7 10
		echo "$response not found"
	fi

	tput cup 16 10
	echo "Any more to update? (Y)es or (N)o> _\b\c"
	read answer
	#
	#	case construct for checking the user selection
	#
	case $answer in
	[Yy]*) answer=y ;;
	*) answer=n ;;
	esac

done

IFS="$OLD_IFS" # restore the IFS to its original value
rm TEMP TTEMP  # delete files

exit 0
