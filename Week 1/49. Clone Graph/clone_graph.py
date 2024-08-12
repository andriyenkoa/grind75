from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q = deque([node])
        clones = {node.val: Node(node.val)}
        while q:
            temp_node = q.popleft()
            cur_clone = clones[temp_node.val]
            for neighbor in temp_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)

                cur_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
