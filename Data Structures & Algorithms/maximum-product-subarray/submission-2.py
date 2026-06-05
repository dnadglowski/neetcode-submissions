class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for x in nums:

            tpm = curMax * x
            curMax = max(tpm, x * curMin, x)
            curMin = min(tpm, x * curMin, x)
            res = max(res,curMax)
        return res