class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                nums[left] = nums[x]
                left += 1

        return left