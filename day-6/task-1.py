class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X: " + str(x) + " Y: " + str(y)


# Manhattan distance
def distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

inp = open("input", "r")
lines = inp.readlines()

field = [[0] * 350 for i in range(350)]
points = []

for line in lines:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])

    points.append(Point(x, y))

for i in range(350):
    for j in range(350):
        min_dist = 20000
        overlap = 0
        for point in points:
            current_point = Point(i, j)
            dist = distance(current_point, point)
            
            if dist == min_dist:
                overlap = 1

            if dist < min_dist:
                field[i][j] = points.index(point)
                min_dist = dist
                overlap = 0

        if overlap == 1:
            field[i][j] = -1

result = 0

for point in points:
    id = points.index(point)
    size = 0

    for i in range(350):
        if field[i][0] == id or field[i][len(field[i]) - 1] == id:
            size = 0
            break
       
        size += field[i].count(id)

    if size > result:
        result = size

print(result)