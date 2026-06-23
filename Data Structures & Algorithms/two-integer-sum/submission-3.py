class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        for i, v in enumerate(nums):
            if v in nums_d:
                return [nums_d[v], i]
            diff = target - v
            nums_d[diff] = i