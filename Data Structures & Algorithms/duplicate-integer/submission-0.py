class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates_hash = {}
        for num in nums:
            if num in duplicates_hash:
                return True
            else:
                duplicates_hash[num]=True
        
        return False
        