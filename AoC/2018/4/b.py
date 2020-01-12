import re
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from pprint import pprint

def update_minutes(m,g):
    if m in minutes:
        if g in minutes[m]:
            minutes[m][g] += 1
        else:
            minutes[m][g] = 1
    else:
        minutes[m] = {g : 1}

def update_guards(g, m):
    if g in guards:
        if m in guards[g]:
            guards[g][m] += 1
        else:
            print "new minute", m, "for", g
            guards[g][m] = 1 
    else:
        print "new", g
        guards[g]={m:1}


datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

p = re.compile('\[(.*)\].*(Guard.#\d+|falls|wakes)')

guard = ''
start = ''
end = ''
times = {}
minutes = {i:{} for i in range(0,59)}
guards = {}

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
            # update all minutes
        while True:
            if start == end:
                break
            minute = int(str(start)[14:-3])
            update_minutes(minute, guard)
            update_guards(guard,minute)
            start = start + timedelta(0,60)



for guard, time in times.iteritems():
    print guard, str(time)

print "minutes", pprint(minutes)
print "guards", pprint(guards)


most = 0
most_id=0
most_g=0
for g in guards:
    for m in guards[g]:
        if guards[g][m] > most:
            most = guards[g][m]
            most_id = m
            most_g = g

print "most", most
print "most_id", most_id
print "most_g", most_g
print "restult", most_id * int(most_g.split('#')[1])
