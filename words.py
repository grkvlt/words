# copyright 2017 by andrew donald kennedy

import sys
import random

people = [ "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle", "I" ]
things = [ "biscuit", "tree", "pencil sharpener", "marmalade", "toast", "fish tank" ]
descriptions = [ "green", "smelly", "tall", "red", "hollow", "musical", "sleepy" ]
actions = [ "ate", "moved", "threw", "copied", "lifted", "found", "missed" ]

def main():
    person = people[int(random.random() * len(people))]
    thing = things[int(random.random() * len(things))]
    description = descriptions[int(random.random() * len(descriptions))]
    action = actions[int(random.random() * len(actions))]

    print "{} {} the {} {}".format(person, action, description, thing)

if __name__ == "__main__":
    main()
