class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = {}
        for start, end, price in flights:
            if start not in graph:
                graph[start] = [(end, price)]
            else:
                graph[start].append((end, price))

        @cache
        def dp(i, moves):
            if moves > k:
                return float("inf")
            if i == dst:
                return 0
            return min(
                (
                    dp(neighbor[0], moves + 1) + neighbor[1]
                    for neighbor in graph.get(i, [])
                ),
                default=float("inf"),
            )

        t = dp(src, -1)
        if t == float("inf"):
            return -1
        return t
