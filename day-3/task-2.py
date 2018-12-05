class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    def __init__(self, p1, p2, id):
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top = max(p1.y, p2.y)
        self.id = id


def range_overlap(a_min, a_max, b_min, b_max):
    return (a_min <= b_max) and (b_min <= a_max)

def overlap(r1,r2):
    return range_overlap(r1.left, r1.right, r2.left, r2.right) and range_overlap(r1.bottom, r1.top, r2.bottom, r2.top)

inp = open("input", "r")
lines = inp.readlines()
zones = []

for line in lines:
    tokens = line.split(" ")
    start_y = int(tokens[2][:-1].split(",")[0])
    start_x = int(tokens[2][:-1].split(",")[1])
    len_y = int(tokens[3].split("x")[0])
    len_x = int(tokens[3].split("x")[1])
    id = int(tokens[0][1:])

    left = Point(start_x, start_y)
    right = Point(start_x + len_x - 1, start_y + len_y - 1)

    zones.append(Rect(left, right, id))

for re1 in zones:
    ok = 0
    for re2 in zones:
        if re1 != re2:
            if overlap(re1, re2) == True:
                ok = 1
    
    if ok == 0:
        print(re1.id)
        exit(0)