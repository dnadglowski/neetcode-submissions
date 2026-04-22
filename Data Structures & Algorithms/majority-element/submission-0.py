class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for x in nums:
            hm[x] = 1 + hm.get(x, 0)

        return(max(hm, key = hm.get))