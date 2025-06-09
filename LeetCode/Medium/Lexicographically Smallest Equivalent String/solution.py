class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjoint_set = {}
        for char1, char2 in zip(s1, s2):
            if char1 in disjoint_set and char2 in disjoint_set:
                val = disjoint_set[char1].union(disjoint_set[char2])
            elif char1 in disjoint_set:
                val = disjoint_set[char1].union(UnionFind(char2))
            elif char2 in disjoint_set:
                val = disjoint_set[char2].union(UnionFind(char1))
            else:
                val = UnionFind(char1).union(UnionFind(char2))
            disjoint_set[char1] = val
            disjoint_set[char2] = val

        result = []
        for char in baseStr:
            if char not in disjoint_set:
                result.append(char)
            else:
                result.append(disjoint_set[char].find().val)
        return "".join(result)

    def is_unique(self, disjoint_set: dict, char: str):
        if char in disjoint_set:
            return False, disjoint_set[char]
        return True, None

class UnionFind:
    def __init__(self, val):
        self.val = val
        self.parent = None

    def find(self):
        if self.parent != None:
            return self.parent.find()
        return self

    def union(self, node):
        curr = self.find()
        node = node.find()
        if node.val < curr.val:
            curr.parent = node
            return node
        if node.val > curr.val:
            node.parent = curr
            return curr
        return curr
