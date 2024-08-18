import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters = collections.Counter(tasks)
        max_val = max(letters.values())
        num_of_tasks_max_occur = sum((1 for task, occ in letters.items() if occ == max_val))
        ans = (max_val - 1) * (n + 1) + num_of_tasks_max_occur

        return max(ans, len(tasks))
