from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            degree[start] += 1
            degree[end] += 1

        leaves = deque([leaf for leaf in range(n) if degree[leaf] == 1])

        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
