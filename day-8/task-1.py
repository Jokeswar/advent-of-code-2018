res = 0

def iterate(values, pos):
    global res
    children_no = values[pos]
    metadata_no = values[pos + 1]
    pos += 2

    for i in range(children_no):
        pos = iterate(values, pos)

    for i in range(metadata_no):
        res += values[pos + i]

    pos += metadata_no

    return pos

inp = open("input", "r")
line = inp.readline()

values = []
tokens = line.split(" ")

for val in tokens:
    values.append(int(val))

p = iterate(values, 0)
print(res)