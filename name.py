# copyright 2017 by andrew donald kennedy

import random

sounds = [
    "zaa", "goo", "fon", "min", "qua", "zok", "ble", "gon", "moo",
    "gum", "plo", "gip", "dra", "foo", "bin", "zip", "cot", "laa" ]

def choose(words):
    return words[int(random.random() * len(words))]

one = choose(sounds)
two = choose(sounds)
three = choose(sounds)
four = choose(sounds)

print "{}{}{}{}".format(one, two, three, four)
