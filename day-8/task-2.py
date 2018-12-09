class Node:
    def __init__(self, start, end, children):
        self.start = start
        self.end = end
        self.children = children

    def __str__(self):
        return str(self.start) + " -> " + str(self.end)


def iterate(values, pos):
    children = []
    start = pos
    children_no = values[pos]
    metadata_no = values[pos + 1]
    pos += 2

    for i in range(children_no):
        ret = iterate(values, pos)
        pos = ret[0]
        children.append(ret[1])

    pos += metadata_no
    node = Node(start, pos, children)

    return (pos, node)

def calculate(values, node):
    res = 0
    start = node.start
    end = node.end
    children_no = values[start]
    metadata_no = values[start + 1]

    if children_no == 0:
        for i in range(metadata_no):
            res += values[end - metadata_no + i]
        return res

    for i in range(metadata_no):
        current_value = values[end - metadata_no + i]
        if current_value <= children_no:
            res += calculate(values, node.children[values[end - metadata_no + i] - 1])

    return res

inp = open("input", "r")
line = inp.readline()

values = []
tokens = line.split(" ")

for val in tokens:
    values.append(int(val))

tree = iterate(values, 0)[1]
res = calculate(values, tree)
print(res)
