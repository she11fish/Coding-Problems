def add(a, b):
    result = []
    # Add zeroes to arrays to have equal length
    while len(a) != len(b):
        if len(a) < len(b):
            a.insert(0, '0')
        elif len(a) > len(b):
            b.insert(0, '0')
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1' and b[i] == '1':
            return ["1", "0"]
        if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
            result.insert(0, '1')
        else:
            result.insert(0, '0')
    return result
class Solution:
    def solve(self, a, b):
        a = list(a)
        b = list(b)
        # Add zeroes to arrays to have equal length
        while len(a) != len(b):
            if len(a) < len(b):
                a.insert(0, '0')
            elif len(a) > len(b):
                b.insert(0, '0')
        
        # Adding
        result = []
        p = '0'
        t = '0'
        for i in range(len(a)-1, -1, -1):
            char_a = a[i]
            char_b = b[i]
            t = add(list(p), list(char_a))
            t = add(t, list(char_b))
            if len(t) == 1:
                result.insert(0, t[0])
                p = '0'
            elif len(t) == 2:
                result.insert(0, t[1])
                p = t[0]
        if p == '1':
            result.insert(0, p)
        return "".join(result)