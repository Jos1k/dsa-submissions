class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_i = s_d.setdefault(s[i], 0)
            s_d[s[i]] = s_i + 1
            t_i = t_d.setdefault(t[i], 0)
            t_d[t[i]] = t_i + 1

        print(s_d)
        print(t_d)
        
        for k,v in s_d.items():
            
            if v != t_d.get(k, 0):
                return False
        
        return True