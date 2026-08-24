class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res=0,0
        s_dict = {}
        for r, v in enumerate(s):
            if v in s_dict:
                l = max(l,s_dict[v]+1)
            
            res = max(res, r + 1 - l)
            s_dict[v]=r

        return res
                