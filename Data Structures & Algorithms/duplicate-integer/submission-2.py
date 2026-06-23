class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        entries = {}
        for r in nums:
            if r in entries: return True
            entries[r] = entries.get(r, 0)
        return False