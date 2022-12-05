import re

f = open("inputs/day5_input.txt", "r")
content = f.read()
raw = content.split("\n")
instructions = [re.findall(r"\d+", x) for x in raw][10:]

crate_stacks = [
    ['B', 'V', 'W', 'T', 'Q', 'N', 'H', 'D'],
    ['B', 'W', 'D'],
    ['C', 'J', 'W', 'Q', 'S', 'T'],
    ['P', 'T', 'Z', 'N', 'R', 'J', 'F'],
    ['T', 'S', 'M', 'J', 'V', 'P', 'G'],
    ['N', 'T', 'F', 'W', 'B'],
    ['N', 'V', 'H', 'F', 'Q', 'D', 'L', 'B'],
    ['R', 'F', 'P', 'H'],
    ['H', 'P', 'N', 'L', 'B', 'M', 'S', 'Z']
]


def crane_operator(dest, origin, quantity, warehouse, super_stacker=False):
    payload = warehouse[origin-1][:quantity]

    print(f"Stack {origin}: {warehouse[origin-1]}, Moving: {payload} to Stack {dest}: {warehouse[dest-1]}")

    if not super_stacker:
        payload.reverse()

    del warehouse[origin-1][:quantity]

    warehouse[dest-1][:0] = payload

    print(f"Now Stack {origin}: {warehouse[origin-1]}, Stack {dest}: {warehouse[dest-1]}")
    return


for inst in instructions:
    int_inst = [int(x) for x in inst]

    crane_operator(
        dest=int_inst[2],
        origin=int_inst[1],
        quantity=int_inst[0],
        warehouse=crate_stacks,
        super_stacker=True
    )

print("".join([x[0] for x in crate_stacks]))
