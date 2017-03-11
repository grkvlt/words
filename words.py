# copyright 2017 by andrew donald kennedy

import random

people = [
    "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle",
    "I", "Granny", "Biggles" ]
things = [
    "biscuit", "tree", "pencil sharpener", "marmalade", "toast",
    "fish tank", "bicycle", "spanner", "door", "LEGO man", "book",
    "cheese", "cat flap", "machine", "space ship", "cake", "apple",
    "pants", "kitten", "dodecahedron", "picture", "waterfall" ]
joining = [
    "the", "a", "my", "our" ]
descriptions = [
    "green", "smelly", "tall", "red", "hollow", "musical", "sleepy",
    "happy", "sad", "exploding", "empty", "silly", "loud", "frightened",
    "squeaky", "sharp", "bright", "slow", "scary" ]
actions = [
    "ate", "moved", "threw", "copied", "lifted", "found", "missed",
    "opened", "closed", "sat on", "drove", "pushed", "cleaned",
    "fought", "listened to", "dropped", "lost" ]

def choose(words):
    return words[int(random.random() * len(words))]

person = choose(people)
thing = choose(things)
join = choose(joining)
description = choose(descriptions)
action = choose(actions)

if random.random() > 0.5:
    description += " " + choose(descriptions)
else:
    description = "very " + description

print "{} {} {} {} {}".format(person, action, join, description, thing)
