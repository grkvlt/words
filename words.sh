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
    voice=$(echo "${words}" |
        cut -d\  -f1 |
        md5sum |
        cut -c1)
    case ${voice} in
        [12])  say -v Daniel ${words} ;;
        [87])  say -v Fiona ${words} ;;
        [a3])  say -v Oliver ${words} ;;
        [0])  say -v Veena ${words} ;;
        [6])  say -v Yuri ${words} ;;
    esac
    sleep 5
done
