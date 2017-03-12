import random, string

sounds = [
    "zaa", "goo", "fon", "min", "qua", "zok", "ble", "gon", "moo", "kip",
    "gum", "plo", "gip", "dra", "foo", "bin", "zip", "cot", "laa", "arr" ]

def choose(sounds):
    i = random.randint(1, len(sounds)) - 1
    return sounds[i]

def name(n):
    name = ""
    for i in range(n):
        name += choose(sounds)
    return name

name = name(random.randint(3, 6))
print string.capwords(name)
