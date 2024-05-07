nums = input().split()
N, K, M = nums
N = int(N)
K = int(K)
M = int(M)

christmas_gifts = input().split()
new_year_gifts = input().split()

counter = 0
k = K
set_start = set(new_year_gifts[K:])
for i in range(len(christmas_gifts)):
    christmas_gift = int(christmas_gifts[i])
    if abs(k - i) >= K and K - christmas_gift in set_start:
        counter += 1
    set_start.remove(new_year_gifts[k])
    if k == N - 1:
        k = 0
    k += 1
print(counter)