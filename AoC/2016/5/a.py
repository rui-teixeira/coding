import re
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from pprint import pprint


chem = ""
for line in open('input.txt'):
    chem = [c for c in line.strip()]

while True:
    print "units", len(chem)
    done = True 
    i = 0
    while i+1 < len(chem):
        if chem[i].isupper() and chem[i+1].islower():
            if chem[i] == chem[i+1].upper():
                # print chem[0:i+2]
                print "delete", chem[i], chem[i+1]
                del chem[i+1]
                del chem[i]
                done = False
                i -= 2
                continue
        elif chem[i+1].isupper() and chem[i].islower():
            if chem[i] == chem[i+1].lower():
                # print chem[0:i+2]
                print "delete", chem[i], chem[i+1]
                del chem[i+1]
                del chem[i]
                done = False
                i -= 2
                continue
        i += 1
    if done:
        print "done"
        break
        
print "units", len(chem)

