import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            group_st = {char: 0 for char in string.ascii_lowercase}
            for s in st:
                group_st[s] = group_st.get(s, 0) + 1
            
            groups.setdefault(tuple(group_st.items()), []).append(st)
        
        return list(groups.values())