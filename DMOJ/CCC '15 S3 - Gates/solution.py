g = int(input())
p = int(input())

root = {}
for i in range(g+1):
    root[i] = i
breakpoint = False

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
def combine(e, r):
    root[find(e)] = find(r)
i = 0
while i < p and not breakpoint:
    e = find(int(input()))
    if e == 0:
        print(i)
        breakpoint = True
        break
    combine(e, e - 1)
    i += 1
if not breakpoint:
    print(p)
