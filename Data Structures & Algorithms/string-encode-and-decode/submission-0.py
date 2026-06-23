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

            # if s_len == '':
            #     break;
                
            s_len_int = int(s_len)
            i+=1;
            str_dec = s[i:s_len_int+i]
            # print(f'I: {i}, S_LEN_int: {str(s_len_int)}, STR_DEC: {str_dec}')
            result.append(str_dec)
            i+=s_len_int+1;

        return result
