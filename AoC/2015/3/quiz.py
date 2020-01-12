def parea(x,y,z):
    xy = x*y
    yz = y*z
    zx = z*x

    area = (xy + yz + zx) * 2.0

    return (area + min(xy, min(yz, zx)))

def ribbon(x,y,z):
    vol = x * y * z
    min_p = 2 * min(x+y,min(y+z, z+x))
    return vol + min_p

f = open('input')
for line in f:
    deli = {}
    y = 0
    x = 0
    x_2 = 0
    y_2 = 0
    for i in range(len(line)):
        if i % 2 == 0:
            if line[i] == '>':
                x_2+=1
            elif line[i] == '<':
                x_2+=-1
            elif line[i] == 'v':
                y_2+=-1
            elif line[i] == '^':
                y_2+=1

            if (x_2,y_2) in deli:
                deli[(x_2,y_2)] += 1
            else:
                deli[(x_2,y_2)] = 1
        else:
            if line[i] == '>':
                x+=1
            elif line[i] == '<':
                x+=-1
            elif line[i] == 'v':
                y+=-1
            elif line[i] == '^':
                y+=1

            if (x,y) in deli:
                deli[(x,y)] += 1
            else:
                deli[(x,y)] = 1

    print len(deli)
# print deli
