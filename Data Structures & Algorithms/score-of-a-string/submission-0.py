class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0 

        for x in range(len(s)- 1):
            v1 = ord(s[x])
            v2 = ord(s[x+1])

            total += abs(v1-v2)

        return total