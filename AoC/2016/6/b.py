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


area = 0 
for j in range(max_y+1):
    for i in range(max_x+1):

        dist_sum = sum([dist(p, i, j) for p in points])
        if dist_sum < 10000:
            area += 1



print "max area", area





