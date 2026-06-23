class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for letter in s:
            if letter in letters:
                letters[letter]+=1
            else:
                letters[letter]=1
        
        for letter in t:
            if letter in letters:
                letters[letter]-=1
            else:
                letters[letter]=1

        for letters_amount in letters.values():
            if letters_amount != 0:
                print(letters_amount)
                return False
        
        return True

            


        