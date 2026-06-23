class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i,j = 0, len(heights)-1

        while i < j:
            volume = (j-i) * min(heights[i], heights[j])
            result = max(result, volume)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return result
        