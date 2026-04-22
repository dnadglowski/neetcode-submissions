class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]

        for x in nums:
            counts[x]+=1

        i = 0

        for x in range(len(counts)):
            for j in range(counts[x]):
                nums[i] = x
                i +=1 
        return nums