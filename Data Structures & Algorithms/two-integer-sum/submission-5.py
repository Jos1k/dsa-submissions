class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looked = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in looked.keys():
                return [min(looked.get(dif), i),max(looked.get(dif), i)]
            looked[nums[i]] = i