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
total_area = 0
total_ribbon = 0
for line in f:
    [x,y,z] = map(int,line.split('x'))
    total_area += parea(x,y,z)
    total_ribbon += ribbon(x,y,z)
print 'total_area', total_area
print 'total ribbon', total_ribbon

