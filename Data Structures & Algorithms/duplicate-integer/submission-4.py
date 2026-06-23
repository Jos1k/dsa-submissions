class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_c = set(nums)

        return len(nums_c) < len(nums)
        
        