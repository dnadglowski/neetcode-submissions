class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = []

        for x, num in enumerate(nums):
            removed_item = nums.pop(x)
            total.append(math.prod(nums))
            nums.insert(x, removed_item)

        return(total)
        