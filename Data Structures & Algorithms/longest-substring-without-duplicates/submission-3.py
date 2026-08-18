class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        substring = set()
        length = 0
        n = len(s)

        for r in range(n):
            while s[r] in substring:
                substring.remove(s[L])
                L += 1
            
            length = max((r-L) + 1, length)
            substring.add(s[r])

        return length