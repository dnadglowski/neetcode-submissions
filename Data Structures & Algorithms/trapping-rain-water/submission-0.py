class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height)
        res = 0
        for x in range(len(height)):
            left = max(height[l:x+1])
            right = max(height[x:r])

            nums = min(left,right)- height[x]

            if nums > 0:
                res += nums

        
        return res
            
            

            