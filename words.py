# copyright 2017 by andrew donald kennedy

import sys
import random

people = [
    "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle", "I"]
things = [
    "biscuit", "tree", "pencil sharpener", "marmalade", "toast", "fish tank",
    "bicycle", "spanner", "door", "LEGO", "book", "cheese" ]
joining = [
    "the", "a", "my", "our", "some" ]
descriptions = [
    "green", "smelly", "tall", "red", "hollow", "musical", "sleepy",
    "happy", "sad", "exploding", "empty", "silly", "loud" ]
actions = [
    "ate", "moved", "threw", "copied", "lifted", "found", "missed",
    "opened", "closed", "sat on", "drove", "pushed", "cleaned" ]

def word(words):
    return words[int(random.random() * len(words))]

def main():
    person = word(people)
    thing = word(things)
    join = word(joining)
    description = word(descriptions)
    action = word(actions)

    print "{} {} {} {} {}".format(person, action, join, description, thing)

if __name__ == "__main__":
    main()
