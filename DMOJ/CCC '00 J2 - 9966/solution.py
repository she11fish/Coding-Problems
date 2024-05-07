def inverse_num(i):
    reversables = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
    if i in reversables:
        return reversables[i]
    else:
        return False
low = int(input())
high = int(input())


counter = 0
for i in range(low, high + 1):
    start = 0
    end = len(str(i)) - 1
    while start <= end:
        if (not inverse_num(str(i)[end])):
            break
        else:
            if str(i)[start] != inverse_num(str(i)[end]):
                break
        start += 1
        end -= 1
    if start > end:
        counter += 1
print(counter)
