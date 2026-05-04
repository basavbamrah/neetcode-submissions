class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) ==0:
            return None
        stack = list()
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        } 
        for i in tokens:
            if i in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(ops[i](a,b))
            else:
                stack.append(i)

        if len(stack)>0:
            return stack[0]
        return None