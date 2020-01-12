import re
from collections import namedtuple

Point = namedtuple('Point', 'x y')
p = re.compile('^(#\d+).@.(\d+),(\d+):.(\d+)x(\d+)')

def parse_square(s):
    # s = '#1 @ 1,3: 4x4' 
    m = p.match(s)
    cid = m.group(1) 
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2  = x1 + int(m.group(4))
    y2 = y1 + int(m.group(5))

    return (Point(x1,y1),Point(x2,y2),cid)

def overlap((a1, a2, c1_), (b1, b2, c2_)):

    dx = min(b2.x, a2.x) - max(a1.x, b1.x)
    dy = min(b2.y, a2.y) - max(a1.y, b1.y)

    if (dx <= 0) | (dy <= 0):
        return 0
    else:
        return dx*dy


fin = open('input.txt')


squares = [parse_square(l.strip()) for l in fin]

for i in range(len(squares)):
    clean = True
    for j in range(len(squares)):
        if i == j:
            continue
        if overlap(squares[i], squares[j]) != 0:
            clean = False 
    if clean:
        print squares[i]

print 'squares', len(squares)
print 'score', clean


