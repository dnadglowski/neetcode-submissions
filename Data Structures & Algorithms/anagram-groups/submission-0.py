class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for x in strs:
            sorted_chars = sorted(x)
            x_sorted = "".join(sorted_chars)
            if x_sorted in hash_map:
                hash_map[x_sorted].append(x)
            else:
                hash_map[x_sorted] = [x]

        return(list(hash_map.values()))
