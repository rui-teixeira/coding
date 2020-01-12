import re
from pprint import pprint
from collections import defaultdict 

def finish(i):
    global items

"""
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin
"""
items = []
requires = defaultdict(list)
p = re.compile('Step.(.).*step.(.)')
for line in open('input.txt'):
    m = p.match(line.strip())
    A = m.group(2)
    B = m.group(1)
    requires[A].append(B)
    if A not in items:
        items.append(A)
    if B not in items:
        items.append(B)

items = sorted(items)    

result = []
    
while len(items):
    print 'items', items
    pprint(requires)
    for i in range(len(items)):
        item = items[i]
        print 'testing', item
        if len(requires[item]) == 0:
            print item, 'is ready'
            # remove done item from required
            for k in requires:
                if item in requires[k]:
                    print k, 'required', item
                    requires[k].remove(item)
                    print k, 'still needs', requires[k]
            items.remove(item)
            result.append(item)
            break
        print item, 'is NOT ready'

                

print 'order', ''.join(result)
print 'remaining', items
    
