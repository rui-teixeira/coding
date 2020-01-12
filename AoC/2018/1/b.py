
current = 0
freqs = set([current])
while True:
    fin = open('input',  'r')

    for line in fin:
        current += float(line.strip())
        if current in freqs:
            print current
            exit(0)
        else:
            freqs.add(current)

