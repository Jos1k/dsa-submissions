class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #pairs [t, i]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                ti = stack[-1][1]
                result[ti] = i - ti
                stack.pop()
            
            stack.append([temp, i])
        
        return result
        