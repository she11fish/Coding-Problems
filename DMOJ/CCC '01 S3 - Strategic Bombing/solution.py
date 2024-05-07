from typing import List

def dfs(graph: dict, visited: set, current: str, middle1: str, middle2: str, target: str, result: List[str]):
    if (current in visited) or (current == target) or (not current):
        if current == target and not current in visited and result:
            result[-1][1] += target
        return
    visited.add(current)
    result[-1][1] += current
    for neighbours in graph[current]:
        for neighbour in neighbours:
            if current == middle1 and neighbour == middle2:
                continue
            dfs(graph, visited, neighbour, middle1, middle2, target, result)

roads = []
current_road = input()

while current_road != "**":
    roads.append(current_road)
    current_road = input()

graph: dict[str, List[int]] = dict()
for (middle1, end) in roads:
    if (not (middle1 in graph)):
        graph[middle1] = [end]
    else:
        graph[middle1].append(end)
    if (not (end in graph)):
        graph[end] = [middle1]
    else:
        graph[end].append(middle1)

routes = [] 
for key1, value in graph.items():
    for key2, value in graph.items():
        routes.append([key1 + key2, ""])
        dfs(graph, set(), "A", key1, key2, "B", routes)
        
counter = 0
for road, route in routes:
    if not "B" in route:
        counter += 1
        if not road in roads: 
            print(road[::-1])
        else:
            print(road)
print(f"There are {counter} disconnecting roads.")