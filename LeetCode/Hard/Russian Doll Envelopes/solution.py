class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        tails = []

        for _, height in envelopes:
            left = 0
            right = len(tails)

            while left < right:
                mid = (left + right) // 2

                if tails[mid] < height:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(height)
            else:
                tails[left] = height
        return len(tails)
