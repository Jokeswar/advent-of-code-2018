from datetime import datetime

inp = open("input", "r")
lines = inp.readlines()

guards = [[0] * 62 for i in range(4000)]
ids = []

id = -1
start = -1
stop = -1

lines.sort()

for line in lines:
    tokens = line.split(" ")
    dateobj = datetime.strptime(tokens[0] + " " + tokens[1], "[%Y-%m-%d %H:%M]")

    if tokens[2] == "Guard":
        id = int(tokens[3][1:])

        if (id in ids) is False:
            ids.append(id)

        start = -1
        stop = -1

    if tokens[2] == "falls":
        start = dateobj.minute
    
    if tokens[2] == "wakes":
        stop = dateobj.minute
        for i in range(start, stop):
            guards[id][i] += 1

ma = 0
id_max = -1
minute = -1
for i in ids:
    if(max(guards[i]) > ma):
        ma = max(guards[i])
        id_max = i
        minute = guards[i].index(max(guards[i]))

print(minute * id_max)
