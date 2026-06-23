class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref_nums = [0] * n
        pref_nums[0] = 1
        
        for i in range(1, n):
            pref_nums[i] = pref_nums[i-1] * nums[i-1]

        suf_nums = [0] * n
        suf_nums[n-1] = 1

        for i in range(n-2, -1, -1):
            suf_nums[i]=suf_nums[i+1] * nums[i+1]
        
        result = [0] * n
        
        for i in range(n):
            result[i] = suf_nums[i] * pref_nums[i]
        
        return result
        




