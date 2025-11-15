def ans(l):
    start = l[0]
    for num in l:
        if int(num) % 2 != int(start) % 2:
            return sorted(l, key=int)
    return l


n = int(input())
res = []
for i in range(n):
    input()
    rest = input().split(" ")
    res.append(" ".join([str(a) for a in ans(rest)]))
for e in res:
    print(e)
