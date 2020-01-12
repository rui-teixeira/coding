from collections import namedtuple, defaultdict
from pprint import pprint

Point = namedtuple('Point', 'x y')

def parsePoint(s):
    [xs, ys] = s.split(', ')
    return Point(int(xs), int(ys))

def sub(p1, p2):
    return Point(p1.x - p2.x, p1.y - p2.y)

def dist(p, x, y):
    return (abs(p.x - x) + abs(p.y - y))


points = [parsePoint(line.strip()) for line in open('input.txt')]

min_x = min(points).x
min_y = min(points, key=(lambda a: a.y)).y
min_point = Point(min_x, min_y)

points = [sub(p,min_point) for p in points]

max_x = max(points).x
max_y = max(points, key=(lambda a: a.y)).y


score = defaultdict(int)
inf = set()

for j in range(max_y+1):
    for i in range(max_x+1):

        distances = sorted([(dist(p, i, j), p) for p in points])
        winner = distances[0][1]

        if i == 0 or j == 0 or i == max_x or j == max_y:
            if winner not in inf:
                inf.add(winner)
            continue

        if distances[0][0] != distances[1][0]:
            # no ties, score!
            score[distances[0][1]] += 1 


area = 0 
for p in score:
    if p not in inf:
        # print p, score[p]
        if score[p] > area:
            area = score[p]


print "max area", area





