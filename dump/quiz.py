
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
count = 0
f = open('input')
for line in f:
    if is_nice(line):
        count +=1
print count


