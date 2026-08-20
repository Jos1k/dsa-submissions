class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, sufix = [0] * len(height), [0] * len(height)

        i,j = 0, len(height)-1
        max_p, max_s = 0,0

        while i < len(height):
            max_p = max(height[i], max_p)
            prefix[i] = max_p
            max_s = max(height[j], max_s)
            sufix[j] = max_s
            i+=1
            j-=1
        
        res = 0

        for i in range(len(height)):
            res += min(prefix[i], sufix[i]) - height[i]
        
        return res