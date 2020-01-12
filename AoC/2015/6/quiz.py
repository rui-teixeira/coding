from bitarray import bitarray


def toggle(x1, y1, x2, y2):


def set_lights(x1, y1, x2, y2, value):
    while y1 <= y2:
        matrix[y1][x1:x2] = True
        y1 += 1

def sum_lights():
    count = 0
    for i in matrix:
        for j in i:
            if j == 1:
                count +=1
    return count


matrix = [bitarray(1000) for x in range(1000)]
for a in matrix:
    a.setall(False)

f = open('input')
set_lights(0,0,999,999,0)
for line in f:
    print '.',
    [x1, y1, x2, y2] = [int(s) for s in str.split() if s.isdigit()]
    if 'turn on' in line:
        set_lights(x1, y1, x2, y2, 1)
    if 'turn off' in line:
        set_lights(x1, y1, x2, y2, 1)
    if 'toggle' in line:
        toggle(x1, y1, x2, y2)

print sum_lights()



