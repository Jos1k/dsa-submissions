class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, s1Counter = 0, Counter(s1)
        for r in range(len(s2)):
            if r-l == len(s1)-1:
                if s1Counter == Counter(s2[l:r+1]): return True
                l+=1

        return False