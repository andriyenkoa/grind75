import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)

        heap = [(-count, word) for word, count in counter.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
