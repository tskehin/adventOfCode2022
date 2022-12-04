import re

f = open("inputs/day4_input.txt", "r")
content = f.read()

pairs = content.split("\n")
nested_pairs = [x.split(",") for x in pairs]

overlap_pairs = []
contained_pairs = []

for pair in nested_pairs:
    num_pair = [re.findall(r"\d+", x) for x in pair]

    sections1 = {*range(int(num_pair[0][0]), int(num_pair[0][1]) + 1)}
    sections2 = {*range(int(num_pair[1][0]), int(num_pair[1][1]) + 1)}

    if len(sections1 & sections2) > 0:
        overlap_pairs.append(num_pair)

    if len(sections1 & sections2) == min(len(sections1), len(sections2)):
        contained_pairs.append(num_pair)

print(len(contained_pairs), len(overlap_pairs))