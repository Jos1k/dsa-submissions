import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1dict = dict.fromkeys(string.ascii_lowercase, 0)
        s2dict = dict.fromkeys(string.ascii_lowercase, 0)
        l = 0
        
        for c in s1: s1dict[c]+=1
        
        for r,v in enumerate(s2):
            s2dict[v]+=1
            if r - l + 1 > len(s1):
                s2dict[s2[l]]-=1
                l+=1
            if s1dict == s2dict: return True

        return False