class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        sorted_list = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_list[:k]]