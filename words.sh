#!/bin/bash
while true
do
    clear
    echo
    tail -6 story.log
    words=$(python words.py | tee -a story.log)
    echo
    echo "${words}" |
        tr "a-z" "A-Z" |
        figlet -c -w $(tput cols)
    echo
    person=$(echo "${words}" |
        cut -d\  -f1)
    case ${person} in
        Ian|Ben|Biggles)
            say -v Daniel ${words} ;;
        Mum|Granny)
            say -v Fiona ${words} ;;
        Andrew|Dad)
            say -v Oliver ${words} ;;
        Katriona|Wyldstyle)
            say -v Veena ${words} ;;
        *)
            say -v Yuri ${words} ;;
    esac
    sleep 5
done
