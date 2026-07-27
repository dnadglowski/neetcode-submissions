class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        hashmap = {}

        for x in range(len(nums)):
            goal = target - nums[x]

            if goal in hashmap:
                return [hashmap[goal], x]

            hashmap[nums[x]] = x





     