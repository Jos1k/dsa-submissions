class Solution:
    delim = '#'

    def encode(self, strs: List[str]) -> str:
        output = ''
        for st in strs:
            output += f"{len(st)}{self.delim}{st}"
        return output

    def decode(self, s: str) -> List[str]:
        i, output = 0, []
        while i < len(s):
            word_l = ''
            while s[i] != self.delim:
                word_l += s[i]
                i += 1
            i += 1
            word_l_i = int(word_l)
            output.append(s[i:i+word_l_i])
            i += word_l_i
        return output

