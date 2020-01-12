import re
from collections import namedtuple
from datetime import datetime
from datetime import timdelta

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

p = re.compile('\[(.*)\].*(Guard.#\d+|falls|wakes)')

guard = ''
start = ''
end = ''
times = {}
sleepy = {}

for line in open('sorted.txt'):
    m = p.match(line.strip())
    action = m.group(2)
    if "Guard" in action:
        guard = action 
    elif "falls" in action:
        start = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
    elif "wakes" in action:
        end = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
        if guard in times:
            times[guard] += (end-start)
        else:
            times[guard] = end-start
        # special case for sleppy
        if "Guard #1549" in guard:
            while True:
                if start == end:
                    break
                if start in sleepy:
                    sleepy[start] += 1
                else:
                    sleepy[start] = 1

                start = start + timedelta(0,60)





for guard, time in times.iteritems():
    print guard, str(time)
print "Guard #1549", str(sleepy)


