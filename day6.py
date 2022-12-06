f = open("inputs/day6_input.txt", "r")
content = f.read()


def parser(datastream, marker_size):
    for i in range(marker_size, len(content)):
        marker = datastream[i - marker_size:i]

        if len(set(marker)) == len(marker):
            break
    return i


print(parser(datastream=content, marker_size=4))
print(parser(datastream=content, marker_size=14))