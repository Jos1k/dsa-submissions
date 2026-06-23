import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
            "**": operator.pow
        }
        operandsStack = []

        for t in tokens:
            if t not in ops:
                operandsStack.append(int(t))
            else:
                operation = ops.get(t)
                b = operandsStack.pop()
                a = operandsStack.pop()
                operandsStack.append(operation(a,b))
            
        return operandsStack.pop()
                