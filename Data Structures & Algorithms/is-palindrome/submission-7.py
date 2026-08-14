class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i<=j:
            while i < j and (s[i].isalpha() or s[i].isnumeric()) is not True: 
                i+=1
            while i < j and (s[j].isalpha() or s[j].isnumeric()) is not True:
                j-=1
                
            if s[i].lower() != s[j].lower(): return False
            
            i+=1
            j-=1

        return True