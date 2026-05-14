class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room, visited):
            if room in visited:
                return
            visited.add(room)
            for e in rooms[room]:
                dfs(e, visited)

        dfs(0, visited)
        return len(visited) == len(rooms)
