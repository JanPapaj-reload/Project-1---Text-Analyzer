import random

# Promicha vlozenou vetu
ordered = input("vloz vetu: ").replace(",.?!-;", " ")
ordered = ordered.split()
random.shuffle(ordered)
result = []
for word in ordered:
    word = word.lower()
    result.append(word)

print(result)

