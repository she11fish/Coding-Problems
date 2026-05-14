class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = [(time[1], time[2])]
            else:
                graph[time[0]].append((time[1], time[2]))
        for i in range(1, n + 1):
            if i not in graph:
                graph[i] = []
        import heapq
        Q = []
        dist = {}
        dist[k] = 0
        heapq.heappush(Q, (0, k))

        for vertex in graph:
            if vertex != k:
                dist[vertex] = float('inf')
                heapq.heappush(Q, (float('inf'), vertex))

        while Q:
            _, u = heapq.heappop(Q)
            for v, w in graph[u]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(Q, (alt, v))
        ans = max(dist.values())
        return ans if ans != float('inf') else -1 

