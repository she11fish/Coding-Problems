class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        def build(s, d, product):
            if "#" not in d:
                d["#"] = [product]
            else:
                d["#"].append(product)
            if s == "":
                return
            if s[0] not in d:
                d[s[0]] = {}
                t = build(s[1:], d[s[0]], product)
            else:
                build(s[1:], d[s[0]], product)

        def search(d, s):
            if s == "":
                return d["#"]
            t = []
            for item in d:
                if s[0] == item:
                    t += search(d[s[0]], s[1:])
            return t

        trie = {}
        for product in products:
            build(product, trie, product)
        l = []
        for i in range(len(searchWord)):
            s = searchWord[: i + 1]
            l.append(sorted(search(trie, s))[:3])
        return l
