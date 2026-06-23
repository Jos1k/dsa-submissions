class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxW,l = 0,0
        sFreq = {}
        
        for r,c in enumerate(s):
            sFreq.setdefault(c, 0)
            sFreq[c]+=1

            maxCharVal = max(sFreq.values())
            
            if r - l + 1 - maxCharVal > k:
                sFreq[s[l]]-=1
                l+=1

            maxW = max(maxW, r - l + 1)

        return maxW