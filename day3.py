from string import ascii_uppercase, ascii_lowercase

f = open("inputs/day3_input.txt", "r")
content = f.read()
backpacks = content.split("\n")

alpha = ascii_lowercase + ascii_uppercase
item_score = dict((v, k+1) for k,v in enumerate(alpha))

dupes = []

for backpack in backpacks:
    comp1 = backpack[:int(len(backpack)/2)]
    comp2 = backpack[int(len(backpack)/2):]

    dupe = set(comp1) & set(comp2)
    dupes.append(dupe.pop())

scores = [item_score[k] for k in dupes]
print(sum(scores))


groups = [backpacks[i:i+3] for i in range(0, len(backpacks), 3)]
badges = []

for group in groups:
    badge = set(group[0]) & set(group[1]) & set(group[2])
    badges.append(badge.pop())

badge_scores = [item_score[k] for k in badges]
print(sum(badge_scores))