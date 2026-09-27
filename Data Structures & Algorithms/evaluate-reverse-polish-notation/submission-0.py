class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = "+-*/"
        stack = []

        for t in tokens:
            if stack and t in calc:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]

                