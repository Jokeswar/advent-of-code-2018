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

SIZE = 500

field = [[0] * SIZE for i in range(SIZE)]
points = []

for line in lines:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])

    points.append(Point(100 + x, 100 + y))

result = 0 

for i in range(SIZE):
    for j in range(SIZE):
        total_dist = 0

        for point in points:
            current_point = Point(i, j)
            total_dist += distance(current_point, point)
            
        if total_dist < 10000:
            result += 1

print(result)