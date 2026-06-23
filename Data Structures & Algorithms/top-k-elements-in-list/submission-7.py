class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            buckets.setdefault(value, []).append(key)
        
        result = []

        for freq in range(len(nums), 0, -1):
            if freq in buckets.keys():
                for val in buckets[freq]:
                    result.append(val)
                    if len(result) == k:
                        return result
        
        return []
