class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[0], height[-1]
        
        while l < r:
            if maxL <= maxR:
                l+=1
                volume = maxL - height[l]
                if volume > 0:
                    result += volume
                maxL = max(maxL, height[l])
            else:
                r-=1
                volume = maxR - height[r]
                if volume > 0:
                    result += volume
                maxR = max(maxR, height[r])
    
        return result