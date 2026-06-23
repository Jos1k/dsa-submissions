class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        maxL = 1
        l = 0
        
        currentS = {
            s[l]:l
        }

        for r in range (1, len(s), 1):
            if s[r] not in currentS:
                currentS[s[r]]=r
                maxL = max(maxL, len(currentS))
            else:
                oldCIndex = currentS[s[r]];
                while l <= oldCIndex:
                    currentS.pop(s[l])
                    l+=1
                currentS[s[r]] = r
        
        return maxL

            