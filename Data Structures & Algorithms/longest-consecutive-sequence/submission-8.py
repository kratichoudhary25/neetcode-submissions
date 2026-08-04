class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        currlen = 1
        maxlen = 0
        num_set = set(nums)
    
        for num in num_set:
            if num - 1 not in num_set:
                currnum = num
                currlen = 1
            
                while (currnum+1) in num_set:
                    currnum += 1
                    currlen += 1

            maxlen = max(currlen, maxlen)

        return maxlen


            
            