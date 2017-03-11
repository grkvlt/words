#!/bin/bash
# copyright 2017 by andrew donald kennedy

# speak the words
while true
do
    words=$(python words.py)
    clear
    echo; echo; echo
    echo ${words} |
        tr "a-z" "A-Z" |
        figlet -c -w $(tput cols)
    say ${words}
    sleep 5
done
