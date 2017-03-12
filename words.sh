#!/bin/bash
while true
do
    words=$(python words.py | tee -a story.log)
    clear
    echo; echo; echo
    echo ${words} |
        tr "a-z" "A-Z" |
        figlet -c -w $(tput cols)
    voice=$((RANDOM % 5))
    case ${voice} in
        0)  say -v Fiona ${words} ;;
        1)  say -v Oliver ${words} ;;
        2)  say -v Yuri ${words} ;;
        3)  say -v Veena ${words} ;;
        4)  say -v Daniel ${words} ;;
    esac
    sleep 5
done
