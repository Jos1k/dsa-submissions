class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        start_seq_nums = {}
        if (len(nums) < 2):
            return len(nums)

        for num in nums:
            if num - 1 not in unique_nums:
                start_seq_nums[num] = 1

        result = 1       
        for num in start_seq_nums:
            i = 1
            while num + i in unique_nums:
                start_seq_nums[num]+=1
                temp_max = start_seq_nums[num]
                
                if temp_max > result:
                    result = temp_max

                i+=1
            if result >= len(nums)/2:
                return result

        return result