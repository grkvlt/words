#!/bin/bash
while true
do
    clear
    echo ; tail -6 story.log | cut -d: -f2 ; echo
    words=$(python words.py)
    person=$(echo "${words}" | cut -d\  -f1)
    case ${person} in
        Ian|Ben|Biggles)
            voice="Daniel" ;;
        Mum|Granny)
            voice="Fiona" ;;
        Andrew|Dad)
            voice="Oliver" ;;
        Katriona|Wyldstyle)
            voice="Veena" ;;
        *)
            words=$(echo "${words}" | sed -E 's/ ((the)|(their)|(this)|(my)|(our)) / /g')
            voice="Yuri" ;;
    esac
    echo "${words}" | tr "a-z" "A-Z" | figlet -c -w $(tput cols)
    echo
    echo "${voice}: ${words}" >> story.log
    say -v ${voice} "${words}"
    sleep 5
done
