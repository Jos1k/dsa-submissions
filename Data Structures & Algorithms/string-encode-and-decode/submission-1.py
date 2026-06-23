class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result+='#'+str(len(s))+'#'+s
        
        return result

    def decode(self, s: str) -> List[str]: 
        result = []
        i = 1
        print(f'str_full: {s}')
        while i < len(s):
            s_len = '';

            while s[i] != '#':
                s_len += s[i]
                i+=1;
                
            s_len_int = int(s_len)
            i += 1;

            result.append(s[i:s_len_int+i])
            
            i+=s_len_int+1;

        return result
