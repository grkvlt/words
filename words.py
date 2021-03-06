import random

people = [
    "Ian", "Ben", "Katriona", "Andrew", "Mum", "Dad", "Wyldstyle", "I", "Granny", "Biggles", "Who", "You", "It",
    "Everyone", "Nobody" ]
actions = [
    "ate", "moved", "threw", "copied", "lifted", "found", "missed", "opened", "closed", "sat on", "drove", "saw",
    "used", "pushed", "cleaned", "fought", "listened to", "dropped", "lost", "made", "took", "wanted", "explained",
    "broke", "followed", "counted", "tied up", "unlocked", "painted", "pointed at", "saved", "removed", "spent",
    "calculated", "wrote", "avoided", "went through", "sold", "connected", "flew over", "climbed", "detected", "is" ]
joining = [
    "the", "my", "our", "their", "this" ]
descriptions = [
    "green", "smelly", "tall", "red", "hollow", "musical", "sleepy", "happy", "sad", "exploding", "empty", "spicy",
    "invisible", "silly", "loud", "frightened", "squeaky", "sharp", "bright", "slow", "scary", "fresh", "square",
    "special", "complicated", "strange", "adjustable", "healthy", "new", "sticky", "clear", "squishy", "twisted",
    "expensive", "wrong", "joined up", "partial", "transparent", "old", "internal", "pretty", "chocolate flavoured" ]
things = [
    "biscuit", "tree", "pencil sharpener", "marmalade", "toast", "fish tank", "bicycle", "spanner", "door", "object",
    "dot", "LEGO man", "book", "cheese", "cat flap", "machinery", "space ship", "fairy cake", "apple", "pair of pants",
    "knife and fork", "kitten", "dodecahedron", "picture", "waterfall", "socks", "sellotape", "honey badger", "parcel",
    "rule", "recipe", "house", "bit of string", "plank of wood", "steam engine", "box", "kettle", "beehive", "pot plant",
    "pound coin", "equation", "fulcrum", "word", "dictionary", "person", "robotic dog", "clothes horse", "top hat" ]

def choose(words):
    i = random.randint(0, len(words) - 1)
    return words[i]

person = choose(people)
action = choose(actions)
join = choose(joining)
description = choose(descriptions)
thing = choose(things)

if random.random() > 0.75:
    description += " " + choose(descriptions)
elif random.random() > 0.67:
    description = "very " + description

if person == "I" and action == "is": action = "am"
if person == "Who": end = "?"
elif random.random() > 0.90: end = "!"
else: end = "."
if random.random() > 0.95: end = ", in space!"

print "{} {} {} {} {}{}".format(person, action, join, description, thing, end)
