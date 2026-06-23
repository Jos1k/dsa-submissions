class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax, sufixMax = [0] * len(height), [0] * len(height)

        for i in range(1, len(height)-1):
            prefixMax[i] = max(height[i-1], prefixMax[i-1])

        for i in range(len(height)-2, -1, -1):
            sufixMax[i] = max(height[i+1], sufixMax[i+1])
        
        result = 0;
        for i in range(len(height)):
            volume = min(prefixMax[i], sufixMax[i]) - height[i]
            if volume > 0:
                result += volume
    
        return result