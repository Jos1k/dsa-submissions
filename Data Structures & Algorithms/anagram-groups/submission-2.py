import string;

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for st in strs:
            key = dict.fromkeys(string.ascii_lowercase, 0)
            for ch in st:
                key[ch]+=1
            group = groups.setdefault(tuple(key.items()), [])
            group.append(st)
        
        output = []
        for group in groups.values():
            output.append(group)
        
        return output