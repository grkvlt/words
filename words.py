# copyright 2017 by andrew donald kennedy

import sys
import random

people = [ "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle", "I" ]
things = [ "biscuit", "tree", "pencil sharpener", "marmalade", "toast", "fish tank" ]
descriptions = [ "green", "smelly", "tall", "red", "hollow", "musical", "sleepy" ]
actions = [ "ate", "moved", "threw", "copied", "lifted", "found", "missed" ]

def word(words):
    return words[int(random.random() * len(words))]

def main():
    person = word(people)
    thing = word(things)
    description = word(descriptions)
    action = word(actions)

    print "{} {} the {} {}".format(person, action, description, thing)

if __name__ == "__main__":
    main()
