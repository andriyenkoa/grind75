import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        email_to_name = {}

        for account in accounts:
            primary_email = account[1]
            email_to_name[primary_email] = account[0]

            for email in account[1:]:
                graph[primary_email].append(email)
                graph[email].append(primary_email)

        res = []
        visited = set()

        for vertex in graph:
            if vertex not in visited:
                visited.add(vertex)
                stack = [vertex]
                temp_res = []
                while stack:
                    node = stack.pop()
                    temp_res.append(node)
                    for edge in graph[node]:
                        if edge not in visited:
                            visited.add(edge)
                            stack.append(edge)
                res.append([email_to_name[vertex]] + sorted(temp_res))

        return res
