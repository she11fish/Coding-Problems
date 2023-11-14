def solution(N):
    results = []
    def convertIntToBin(N):
        i = N
        while i != 1:
            if (i % 2 == 0): results.append("0")
            if (i % 2 == 1): results.append("1")
            i = i // 2
        results.append("1")
        return "".join(results[::-1])
    binString = str(convertIntToBin(N))
    l = 0
    r = 0
    found_left_one = False
    found_right_one = False
    maximum = 0
    while l < len(binString) and r < len(binString):
        if binString[l] == "1":
            found_left_one = True
        if binString[r] == "1":
            found_right_one = True
        if found_left_one and found_right_one:
            if maximum < r - l - 1:
                maximum = r - l - 1
            l = r
            found_right_one = False
        if found_left_one:
            r += 1
        else:
            l += 1
            r += 1
    return maximum
