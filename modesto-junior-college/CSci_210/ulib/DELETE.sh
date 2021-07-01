#!/bin/bash
#
# Author: August Frisk
# Course: CSci 210 - Spring 2018
# Assign: Project 06
# File: DELETE.sh
#
# UNIX Library
# DELETE: This program deletes a specified record from the ULIB_FILE.
#         It asks the Author/Title of the book, and displays the specified
#	      book, and deletes it after confirmation, or shows an error message
#	      if the book is not found in the file.
#

OLD_IFS="$IFS" # save the IFS setting

answer=y                    # initialize the answer to indicate yes
while [ "$answer" = y ]; do # as long as the answer is yes
	tput clear
	tput cup 3 5
	echo "Enter the Author/Title> _\b\c"
	read response
	grep -i "$response" ULIB_FILE >TEMP # find specified book in the library

	if [ -s TEMP ]; then # if it is found

		IFS=":" # set IFS to colon
		read title author category status bname date <TEMP

		tput cup 5 10
		echo "UNIX Library - ${BOLD}DELETEMODE${NORMAL}"
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

		if [ "$status" = "out" ]; then

			tput cup 11 14
			echo "Checked out by: $bname"
			tput cup 12 24
			echo "Date: $date"
		fi

		tput cup 13 20
		echo "Delete this book? (Y)es or (N)o>_\b\c"
		read answer

		if [ $answer = y -o $answer = Y ]; then # test for Y or Yy
			grep -iv "$title:$author:$category:$status:$bname:$date" ULIB_FILE >TEMP
			mv TEMP ULIB_FILE
		fi

	else # if book not found
		tput cup 7 10
		echo "$response not found"
	fi

	tput cup 15 10
	echo "Any more to delete? (Y)es or (N)o> _\b\c"
	read answer
	#
	#	case construct for checking the user selection
	#
	case $answer in
	[Yy]*) answer=y ;;
	*) answer=n ;;
	esac

done

IFS="OLD_IFS" # restore the IFS to its original value
rm TEMP

exit 0
