import re
from pprint import pprint
from collections import defaultdict, namedtuple

Worker = namedtuple('Worker', 'item time')

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

def cost(item):
    global time
    return ord(item) - ord('A') + 1 + 60 + time

def start(item):
    global workers
    global items
    global time
    workers.append(Worker(item, cost(item)))
    items.remove(item)
    print 'starting', item
    print 'ongoing is', workers
    print 'remaining is', items
    print 'time is ', time

def done(item):
    print item, 'is done'
    global requires
    global result
    for k in requires:
        if item in requires[k]:
            print k, 'required', item
            requires[k].remove(item)
            print k, 'still needs', requires[k]
    result.append(item)

def is_finished():
    global workers
    global items
    return len(items) == 0 and len(workers) == 0

workers = []
time = 0
while True:
    #raw_input("Press Enter to continue... " + str(time))
    work_done = False
    for i in range(len(workers)):
        worker = workers[i]
        if worker.time == time:
            done(worker.item)
            work_done = True 
            del workers[i]
            print 'done', worker.item, '@', worker.time
            print 'items are', items
            print 'result is', result
            print 'ongoing is', workers 
            print 'time is', time
            if is_finished():
                exit(0)
            break

    if work_done:
        continue
    
    for item in items:
        # print 'checking',item
        if len(requires[item]) == 0 and len(workers) < 5:
            start(item)
    time += 1
                
