class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        nums_fr = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        for i, v in nums_dict.items():
            nums_fr.setdefault(v,[]).append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            if i in nums_fr:
                for fr in nums_fr[i]:
                    res.append(fr)
                    if len(res) == k:
                        return res
        return res