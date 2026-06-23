class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums_s = sorted(nums)

        for i in range(len(nums)-2):
            j,k = i+1, len(nums_s)-1
            while j < k:
                if nums_s[i] + nums_s[j] + nums_s[k] > 0:
                    k -= 1
                elif nums_s[i] + nums_s[j] + nums_s[k] < 0:
                    j += 1
                else:
                    triplets.add((nums_s[i], nums_s[j], nums_s[k]))
                    k -= 1
                    j += 1

        return [list(t) for t in triplets]
        