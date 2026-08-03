class Solution:
    delim = '#'

    def encode(self, strs: List[str]) -> str:
        output = ''
        for st in strs:
            output += f"{len(st)}{self.delim}{st}"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        if len(s) == 0:
            return output

        i = 0
        while i < len(s):
            word_l = ''
            while s[i] != self.delim:
                word_l += s[i]
                i += 1
            i += 1
            output.append(s[i:i+(int(word_l))])
            i += int(word_l)

        return output

