import random

people = [
    "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle", "I", "Granny", "Biggles", "Who", "You", "It" ]
actions = [
    "ate", "moved", "threw", "copied", "lifted", "found", "missed", "opened", "closed", "sat on", "drove",
    "pushed", "cleaned", "fought", "listened to", "dropped", "lost", "made", "took" ]
joining = [
    "the", "my", "our", "their" ]
descriptions = [
    "green", "smelly", "tall", "red", "hollow", "musical", "sleepy", "happy", "sad", "exploding", "empty",
    "silly", "loud", "frightened", "squeaky", "sharp", "bright", "slow", "scary", "fresh", "square", "special" ]
things = [
    "biscuit", "tree", "pencil sharpener", "marmalade", "toast", "fish tank", "bicycle", "spanner", "door",
    "LEGO man", "book", "cheese", "cat flap", "machine", "space ship", "cake", "apple", "pair of pants",
    "kitten", "dodecahedron", "picture", "waterfall", "socks" ]

def choose(words):
    i = random.randint(1, len(words)) - 1
    return words[i]

person = choose(people)
action = choose(actions)
join = choose(joining)
description = choose(descriptions)
thing = choose(things)

if random.random() > 0.667:
    description += " " + choose(descriptions)
elif random.random() > 0.5:
    description = "very " + description

if  person == "Who": end = "?"
elif random.random() > 0.9: end = "!"
else: end = "."

print "{} {} {} {} {}{}".format(person, action, join, description, thing, end)
