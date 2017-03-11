# copyright 2017 by andrew donald kennedy

import sys
import random

sounds = [
    "zaa", "goo", "fon", "min", "qua", "zok", "ble", "gon", "moo",
    "gum", "plo", "gip", "dra", "foo", "bin", "zip", "cot", "laa" ]

def choose(words):
    return words[int(random.random() * len(words))]

def main():
    one = choose(sounds)
    two = choose(sounds)
    three = choose(sounds)
    four = choose(sounds)

    print "{}{}{}{}".format(one, two, three, four)

if __name__ == "__main__":
    main()
