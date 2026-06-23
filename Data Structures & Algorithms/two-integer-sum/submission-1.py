class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        for i, v in enumerate(nums):
            if v in nums_d:
                return [min(i, nums_d[v]), max(i, nums_d[v])]
            diff = target - v
            nums_d[diff] = i
        
        return []