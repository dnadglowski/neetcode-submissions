class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sub = target - nums[i]

            for x in range(i+1, len(nums)):
                if (nums[x] == sub):
                    return [i, x]