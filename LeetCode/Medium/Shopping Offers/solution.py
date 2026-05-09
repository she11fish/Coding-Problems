class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        def dp(track):
            min_total = float("inf")
            i = 0
            while i < len(price) and track[i] == needs[i]:
                i += 1
            if i >= len(price):
                return 0
            if tuple(track) in memo:
                return memo[tuple(track)]
            if track[i] < needs[i]:
                track[i] += 1
                min_total = min(min_total, dp(track) + price[i])
                track[i] -= 1
            for row in special:
                is_valid = True
                for k in range(len(row) - 1):
                    if track[k] + row[k] > needs[k]:
                        is_valid = False
                        break
                if not is_valid:
                    continue
                for k in range(len(row) - 1):
                    track[k] += row[k]
                min_total = min(min_total, dp(track) + row[-1])
                for k in range(len(row) - 1):
                    track[k] -= row[k]
            if min_total == float("inf"):
                min_total = 0
            memo[tuple(track)] = min_total
            return min_total
        return dp([0] * len(price))