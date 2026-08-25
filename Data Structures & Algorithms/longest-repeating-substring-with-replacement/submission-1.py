class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_c_v, most_c_f = s[0], 1
        res = 0
        l = 0
        dict_c = {}

        for r in range(len(s)):
            cur_c = dict_c.get(s[r], 0)
            dict_c[s[r]] = cur_c+1
            
            if most_c_f < dict_c[s[r]]:
                most_c_f = dict_c[s[r]]
                most_c_v = s[r]


            if most_c_f + k < r - l+1:
                dict_c[s[l]]-=1
                l+=1
                if most_c_f < dict_c[s[l]]:
                    most_c_f = dict_c[s[l]]
                    most_c_v = s[l]
            else:
                res = max(res, r-l+1)
        
        return res
                

            



