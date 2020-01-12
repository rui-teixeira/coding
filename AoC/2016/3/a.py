import re
from collections import namedtuple



def parse_claim(s):
    # s = '#1 @ 1,3: 4x4' 
    global squares
    m = p.match(s)
    cid = m.group(1) 
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2  = x1 + int(m.group(4))
    y2 = y1 + int(m.group(5))

    global highlander
    candidate = cid
    for j in range(y1 - 1, y2 - 1):
        for i in range (x1 - 1, x2 - 1):
            if squares[j][i] != 0:
                candidate = highlander
            squares[j][i] += 1
    highlander = candidate

Point = namedtuple('Point', 'x y')
p = re.compile('^(#\d+).@.(\d+),(\d+):.(\d+)x(\d+)')

fin = open('input.txt')

a = 1000

squares = [[0]*a for _ in range(a)]

highlander = ''


for line in open('input.txt'):
    parse_claim(line.strip())

print squares[0], len(squares[0])
print squares[999], len(squares[999])

score = 0
for j in range(len(squares)):
    for i in range(len(squares[j])):
        if squares[j][i] >= 2:
            score += 1

print "score", score
print "highlander", highlander

