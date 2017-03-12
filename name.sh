#!/bin/bash
while true
do
    clear
    echo ; echo
    name=$(python name.py)
    echo ${name} |
        figlet -c -w $(tput cols)
    say -v Daniel ${name}
    sleep 1
done
