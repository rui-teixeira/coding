


def check(s):
    freq = {}
    found_dup = 0
    found_trip = 0
    for c in s:
        if c in freq.keys():
            freq[c]+=1
        else:
            freq[c]=1

    for k,v in freq.iteritems():
        if v == 3:
            found_trip = 1
        if v == 2:
            found_dup = 1

    return found_dup, found_trip


dups = 0
trips = 0

while True:
    fin = open('input',  'r')

    for line in fin:
        found_dup, found_trip = check(line.strip())
        dups += found_dup
        trips += found_trip

    print dups * trips

    exit(0)
