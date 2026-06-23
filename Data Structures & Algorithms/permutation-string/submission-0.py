class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, s1Dic, wDic = 0, {},{}
        
        for c in s1:
            s1Dic[c] = s1Dic.get(c, 0) + 1
        
        for r in range(len(s2)):
            wDic[s2[r]] = wDic.get(s2[r], 0) + 1

            if r-l == len(s1)-1:
                if s1Dic == wDic: return True
                else:
                    if wDic.get(s2[l],0) <= 1: wDic.pop(s2[l])
                    else: wDic[s2[l]]-=1
                    l+=1

        return False