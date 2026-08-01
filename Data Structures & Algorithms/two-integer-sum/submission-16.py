class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in nummap:
                return [nummap[comp], i]
            nummap[num] = i