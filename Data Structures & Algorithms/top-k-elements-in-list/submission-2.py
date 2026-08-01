from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        counts = c.most_common(k)
        return [item[0] for item in c.most_common(k)]
