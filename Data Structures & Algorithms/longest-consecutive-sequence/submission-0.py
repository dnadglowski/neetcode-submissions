class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        count = 0 

        for x in numSet:
            if x-1 not in numSet:
                tmp = 0
                y = x
                while (y in numSet):
                    tmp += 1
                    y += 1
                count = max(count, tmp)
        return count
                    