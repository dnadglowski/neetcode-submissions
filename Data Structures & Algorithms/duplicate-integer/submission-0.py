class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums:
            if num in hash_table:
                return True
            else:
                 hash_table.update({num: '0'})
        return False