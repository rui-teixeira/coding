
bad_list = ['ab', 'cd', 'pq', 'xy']
def is_nice(s):
    for word in bad_list:
        if word in s:
            return False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            break
    else:
        return False
    count = 0
    for l in s:
        if l in 'aeiou':
            count += 1
        if count > 2:
            break
    else:
        if count < 3:
            return False
    return True

def is_nice_new(s):

    for i in range(len(s)):
        try:
            if s[i] == s[i+2]:
                break
        except:
            return False
    else:
        return False

    slices = [s[i:i+2] for i in range(len(s)-1)]
    for sli in slices:
        if s.find(sli, s.find(sli)+2) > 0:
            break
    else:
        return False

    return True

count = 0
f = open('input')
for line in f:
    if is_nice_new(line.strip()):
        count +=1
print count


