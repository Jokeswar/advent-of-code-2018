import networkx

inp = open("input", "r")
lines = inp.readlines()

G = networkx.DiGraph()

for line in lines:
    tokens = line.split(" ")
    step1 = tokens[1]
    step2 = tokens[7]
    G.add_edge(step1, step2)

print(''.join(networkx.lexicographical_topological_sort(G)))