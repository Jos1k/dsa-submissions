class Solution:
    def isValid(self, s: str) -> bool:
        openBracketsStack = []
        for b in s:
            if b in ["(", "{", "["]:
                openBracketsStack.append(b)
            elif len(openBracketsStack) > 0:
                if b == ")":
                    lastOpenBracket = openBracketsStack.pop()
                    if lastOpenBracket != "(":
                        return False
                elif b == "}":
                    lastOpenBracket = openBracketsStack.pop()
                    if lastOpenBracket != "{":
                        return False
                elif b == "]":
                    lastOpenBracket = openBracketsStack.pop()
                    if lastOpenBracket != "[":
                        return False
            else:
                return False
        
        if len(openBracketsStack) == 0:
            return True
        else:
            return False