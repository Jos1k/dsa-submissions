class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_D = {}

        for c in s:
            s_D[c] = s_D.get(c, 0) + 1
        
        for c in t:
            if c in s_D:
                s_D[c] = s_D.get(c, 0) - 1
                if s_D[c] <= 0:
                    s_D.pop(c)
            else: return False
        
        return len(s_D) == 0
