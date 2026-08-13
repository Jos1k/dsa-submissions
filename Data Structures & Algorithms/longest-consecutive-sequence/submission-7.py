class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0

        nums_u, nums_s, max_s = set(nums), [], 1

        for n in nums_u:
            if n - 1 not in nums_u:
                cur, cur_l = n, 1
                while cur + 1 in nums_u:
                    cur += 1
                    cur_l += 1
                max_s = max(cur_l, max_s)
        
        return max_s