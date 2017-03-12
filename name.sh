#!/bin/bash
aiff="${TMPDIR}/${RANDOM}.aiff"
trap "rm ${aiff} ; exit 0" 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
while true
do
    clear
    echo ; echo
    name=$(python name.py)
    echo ${name} |
        figlet -w $(tput cols) |
        sed -e "s/^/    /g"
    sleep 1
    say -v Daniel "${name}"
    echo
    orig=$(echo "/ ${name} /" |
        tr "a-z" "A-Z" |
        sed -e "s/\([A-Z][A-Z][A-Z]\)/\1-/g" |
        sed -e "s/- \/$/ \//" |
        sed -e "s/-/ - /g")
    n=$(grep "^..........." /usr/share/dict/words | wc -l)
    i=$((RANDOM % n))
    word=$(grep "^..........." /usr/share/dict/words |
        tail +${i} |
        head -1 |
        tr "A-Z" "a-z")
    echo "        ${orig} (${word})"
    say -v Daniel --file-format=AIFF -o ${aiff} "${name}"
    play --no-show-progress "|sox ${aiff} -p speed 0.85 stretch 1.35" \
        chorus 0.8 0.8 60 0.5 0.5 6 -t
    sleep 2
    say -v Daniel "${name}"
    sleep 4
done
