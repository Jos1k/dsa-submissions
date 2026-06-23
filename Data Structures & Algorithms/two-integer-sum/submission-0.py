class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in differences:
                return [differences[dif], i]
            differences[nums[i]]=i