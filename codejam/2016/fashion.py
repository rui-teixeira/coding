#!/usr/bin/python3

cases = int(input())


def answer(case, a):
    print("Case #{}: {}".format(case + 1, len(a)))
    print("\n".join(a))



def calc(j, p, s, k):
    res = []
    p_counter = 0
    s_counter = 0
    for ji in range(j):
        for pi in range(p):
            p_counter += 1
            if p_counter > k:
                p_counter = 0
                break
            for si in range(s):
                s_counter += 1
                if s_counter > k:
                    s_counter = 0
                    break
                res.append("{} {} {}".format(ji+1, pi+1, si+1))
    return res

for case in range(cases):
    [j, p, s, k] = [int(i) for i in input().split()]
    res = calc(j, p, s, k)
    answer(case, res)


