class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0]
        currSum = 0

        for x in nums:
            if currSum < 0:
                currSum = 0
            currSum += x
            maxSub = max(maxSub, currSum)

        return maxSub