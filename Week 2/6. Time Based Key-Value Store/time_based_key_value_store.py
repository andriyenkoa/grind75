import collections


class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(dict)
        self.timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        left, right = 0, len(self.timestamps[key]) - 1
        while left < right:
            mid = (left + right) // 2
            if timestamp > self.timestamps[key][mid]:
                left = mid + 1
            else:
                right = mid
        if self.timestamps[key][left] > timestamp:
            if left == 0:
                return ""
            left -= 1
        return self.dict[key][self.timestamps[key][left]]
