inp = open("input", "r")
lines = inp.readlines()
inches = 0
cloth = [[0] * 2000 for i in range(2000)]

for line in lines:
    tokens = line.split(" ")
    start_y = int(tokens[2][:-1].split(",")[0])
    start_x = int(tokens[2][:-1].split(",")[1])
    len_y = int(tokens[3].split("x")[0])
    len_x = int(tokens[3].split("x")[1])

    for i in range(start_x, start_x + len_x):
        for j in range(start_y, start_y + len_y):
            cloth[i][j] += 1

for line in cloth:
    for elem in line:
        if elem > 1:
            inches += 1
        
print(inches)