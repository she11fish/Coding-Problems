with open("shell.in", mode="r") as f:
    N = int(f.readline())
    choices = []
    for i in range(N):
        a, b, q = f.readline().split()
        choices.append((int(a), int(b), int(q)))
shells = [0, 0, 0]
counter = 0
for i in range(len(shells)):
    shells[i] = 1
    curr_counter = 0
    for choice in choices:
        q = choice[2]
        a, b = choice[0], choice[1]
        shells[a-1], shells[b-1] = shells[b-1], shells[a-1] 
        if shells[q]:
            curr_counter += 1
            counter = max(curr_counter, counter)
    shells = [0, 0, 0]
with open("shell.out", mode="w") as f:
    f.write(str(counter))