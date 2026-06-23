class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_c = set()

        for n in nums:
            if n in nums_c:
                return True
            else:
                nums_c.add(n)
        
        return False
        
        