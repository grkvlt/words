#!/bin/bash
story="${TMPDIR}story.$(date +%Y%m%d%H%M%S).log"
trap "echo ; echo ${story} ; exit 0" 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
while true ; do
    clear
    echo
    test -f ${story} && ( tail -6 ${story} | cut -d: -f2 )
    echo
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
        *)  voice="Yuri"
            words=$(echo "${words}" | sed -E 's/ ((the)|(their)|(this)|(my)|(our)) / /g') ;;
    esac
    echo "${words}" | tr "a-z" "A-Z" | figlet -c -w $(tput cols)
    echo
    echo "${voice}: ${words}" >> ${story}
    say -v ${voice} "${words}"
    sleep 5
done
