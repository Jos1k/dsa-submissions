class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            res = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    res += 1
                else:
                    result.append(res + 1)
                    break
            
            if res + i + 1 == len(temperatures):
                result.append(0)
        
        return result
        