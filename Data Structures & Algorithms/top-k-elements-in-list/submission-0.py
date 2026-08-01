class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = set(nums)
        counts = {key:0 for key in n}

        for i in nums:
            counts[i] += 1

        sorted_items_asc = sorted(counts.items(), key=lambda item: item[1])
        counts = dict(sorted_items_asc)
        numbers = list(counts.keys())
        return numbers[-k:]