class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_c_f = 1
        res = 0
        l = 0
        dict_c = {}

        for r in range(len(s)):
            cur_c = dict_c.get(s[r], 0)
            dict_c[s[r]] = cur_c+1

            most_c_f = max(most_c_f, dict_c[s[r]])

            if most_c_f + k < r - l + 1:
                dict_c[s[l]]-=1
                l+=1
                most_c_f = max(most_c_f, dict_c[s[l]])
            
            res = max(res, r-l+1)
        
        return res
                

            



