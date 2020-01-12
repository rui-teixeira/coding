import re
import string
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from pprint import pprint


def process(chem, debug=False):
    # print chem
    while True:
        done = True 
        i = 0
        while i+1 < len(chem):
            if chem[i].isupper() and chem[i+1].islower():
                if chem[i] == chem[i+1].upper():
                    if debug:
                        print chem[i-2:i+2]
                    del chem[i+1]
                    del chem[i]
                    done = False
                    i -= 2
                    continue
            elif chem[i+1].isupper() and chem[i].islower():
                if chem[i] == chem[i+1].lower():
                    if debug:
                        print chem[i-2:i+2]
                    del chem[i+1]
                    del chem[i]
                    done = False
                    i -= 2
                    continue
            i += 1
        if done:
            break
    return chem
        
master_chem = ""
for line in open('input.txt'):
    master_chem = [c for c in line.strip()]

score = len(process([a for a in master_chem]))

print "a", score 

scores = {}
min_s = ''
min_v = 999999999999999999999999
for s in string.ascii_lowercase:
    S = s.upper()
    debug = False
    score = len(process([c for c in master_chem if (c!=s and c!=S)], debug=debug))
    print s, score
    if score < min_v:
        min_v = score
        min_s = s

print min_s, min_v

