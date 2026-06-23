class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums_s = sorted(nums)

        for i in range(len(nums_s)-2):
            if nums_s[i] > 0:
                break
            
            if i > 0 and nums_s[i] == nums_s[i-1]:
                continue

            j,k = i+1, len(nums_s)-1
            while j < k:
                if nums_s[i] + nums_s[j] + nums_s[k] > 0:
                    k -= 1
                elif nums_s[i] + nums_s[j] + nums_s[k] < 0:
                    j += 1
                else:
                    triplets.append((nums_s[i], nums_s[j], nums_s[k]))
                    k -= 1
                    j += 1

                    while nums_s[j] == nums_s[j-1] and j < k:
                        j += 1

        return triplets;
        