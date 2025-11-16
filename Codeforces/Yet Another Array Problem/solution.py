from math import gcd


def ans(l):
    g = gcd(*l)
    for i in range(2, 10**9):
        if gcd(g, i) == 1:
            return i
    return -1


n = int(input())
res = []
for i in range(n):
    input()
    rest = [int(num) for num in input().split(" ")]
    res.append(str(ans(rest)))
for e in res:
    print(e)
