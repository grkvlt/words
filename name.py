import random

sounds = [
    "zaa", "goo", "fon", "min", "qua", "zok", "ble", "gon", "moo", "kip",
    "gum", "plo", "gip", "dra", "foo", "bin", "zip", "cot", "laa", "arr" ]

def choose(words):
    return words[int(random.random() * len(words))]

def name(n):
    name = ""
    for i in range(n):
        name += choose(sounds)
    return name

print name(5)
