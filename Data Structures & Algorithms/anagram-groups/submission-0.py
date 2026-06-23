class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            letters_dict = [0] * 26
            for letter in str:
                letter_index = ord(letter) - ord('a')
                letters_dict[letter_index]+=1
            result.setdefault(tuple(letters_dict), []).append(str)
        
        return list(result.values())

        