class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for y in range(len(nums)):
                    if i != j and j != y and i != y:
                        if nums[i] + nums[j] + nums[y] == 0:
                            triplets.add(tuple(sorted([nums[i], nums[j], nums[y]])))

        return [list(t) for t in triplets]
        