


def diff(w1, w2):
    counter = 0
    common = ""
    for i in xrange(len(w1)):
        if w1[i] == w2[i]:
            counter += 1
            common += w1[i]
    return counter, common


dups = 0
trips = 0

while True:
    fin = open('input',  'r')

    words = [line.strip() for line in fin]
    pairs = {}
    
    for i in xrange(len(words)):
        for j in xrange(i, len(words)):
            count, inter = diff(words[i], words[j])
            pairs[count] = inter

    print pairs[len(words[0])-1]


    exit(0)
