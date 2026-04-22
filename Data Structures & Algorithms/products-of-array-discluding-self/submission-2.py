class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
    # Build prefix (exclusive)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
    
    # Build postfix (exclusive)
        postfix = [1] * n
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
    
    # Multiply prefix and postfix
        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * postfix[i]
    
        return result