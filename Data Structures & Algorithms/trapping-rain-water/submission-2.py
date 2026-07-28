class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        res = 0
        maxl= 0
        maxr =0
        while l < r:
            if maxl < height[l]:
                maxl = height[l]
            if maxr < height[r]:
                maxr = height[r]

            if maxl > maxr:
                r -= 1
                temp = maxr -height[r]
                if temp > 0:
                    res += temp
            else:
                l += 1
                temp = maxl -height[l]
                if temp > 0:
                    res += temp
            
        return res

            