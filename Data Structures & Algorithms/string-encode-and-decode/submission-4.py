class Solution:

    def encode(self, strs: List[str]) -> str:
        outputstr = []
        for st in strs:
            outputstr.append(str(len(st)) + '#' + st)

        return ''.join(outputstr)


    def decode(self, s: str) -> List[str]:
        # if s == '': return ['']
        i, out_list = 0, []
        while i < len(s):
            nums = ''
            while s[i]!='#':
                nums += s[i]
                i+=1
            i+=1
            num = int(nums)
            out_list.append(s[i:i+num])
            i+=num
        return out_list
            


            
