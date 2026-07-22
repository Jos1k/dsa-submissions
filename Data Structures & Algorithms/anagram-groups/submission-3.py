import string;

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for st in strs:
            key = dict.fromkeys(string.ascii_lowercase, 0)
            for ch in st:
                key[ch] = key.get(ch, 0) + 1
            
            groups.setdefault(tuple(key.items()), []).append(st)
        
        return list(groups.values())