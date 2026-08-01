class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for token in tokens:
            if token in "+-*/":
                b = self.stack.pop()
                a = self.stack.pop()
                if token == "+":
                    value = a + b
                if token == "-":
                    value = a - b
                if token == "*":
                    value = a * b
                if token == "/":
                    value = int(a / b)
            else:
                value = int(token)
            print(value)
            self.stack.append(value)
        return self.stack[-1]