f = open("inputs/day1_input.txt", "r")
content = f.read()

raw_elves = content.split("\n\n")
elves_dict = {}

for elf, load in enumerate(raw_elves):
    items = [int(x) for x in load.split("\n")]
    elves_dict[f"Elf {elf + 1}"] = sum(items)

elf_totals = sorted(elves_dict.values(), reverse=True)

print(elf_totals[0])
print(sum(elf_totals[:3]))

