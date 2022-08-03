class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        if not trust:
            return -1
        
        graph = {}
        
        # Create a Graph
        for nums in trust:
            if not nums[0] in graph:
                graph[nums[0]] = {nums[1]}
            else:
                graph[nums[0]].add(nums[1])
            if not nums[1] in graph:
                graph[nums[1]] = set()
        print(graph)
        
        # Decide judge exists
        judge = None
        for key, value in graph.items():
            if value == set():
                if judge == None:
                    judge = key
                else:
                    return -1
        if judge == None:
            return -1
        
        # Check if all people trust judge
        for key, value in graph.items():
            if not judge in value and key != judge:
                return -1
            
        return judge 