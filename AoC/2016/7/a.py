from collections import defaultdict
from pprint import pprint
import re

work = defaultdict(list) 


def parse(line, p):
    m = p.match(line)
    return m.group(1), m.group(2)

pattern = re.compile('Step (.).*step (.)')

items = set([]) 

for line in open('input.txt'):
    k, v = parse(line, pattern)
    items.add(v)
    work[k].append(v)

# pprint(items)
# pprint(work)

available = []
for k in work:
    if k not in items:
        available.append(k)

print available









