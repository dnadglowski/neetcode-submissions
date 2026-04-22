class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)== len(t):
            hash_table = {}
           
            for char in s:
                if char in hash_table:
                    hash_table[char] += 1
                else: 
                    hash_table.update({char : 1}) 
            for chars in t:
                if chars in hash_table:
                    hash_table[chars] -= 1
                else: 
                    return False
            if any(value < 0 for value in hash_table.values()):
                return False
            else:
                return True 
        else:
            return False