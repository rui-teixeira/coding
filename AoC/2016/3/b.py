import re
from collections import namedtuple
from PIL import Image

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
            if squares[j][i] == 0:
                squares[j][i] = 1
            elif squares[j][i] == 1:
                candidate = highlander
                squares[j][i] = 2
    # print cid, candidate
    highlander = candidate

Point = namedtuple('Point', 'x y')
p = re.compile('^(#\d+).@.(\d+),(\d+):.(\d+)x(\d+)')

fin = open('input.txt')

a = 1000

squares = [[0]*a for _ in range(a)]

highlander = ''


for line in open('input.txt'):
    parse_claim(line.strip())

score = 0
for j in range(len(squares)):
    for i in range(len(squares[j])):
        if squares[j][i] >= 2:
            score += 1

img = Image.new( 'RGB', (1000,1000), 'black') # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        s = squares[j][i]
        if s == 0:
            pixels[i,j] = (250, 250, 250) # Set the colour accordingly
        else:
            pixels[i,j] = (255-s*30, 255-s*30, 255-s*30) # Set the colour accordingly
img.show()

print "score", score
print "highlander", highlander

