# Reverse Polish Notation (Evaluation of postfix expression)
class Solution:
    def evalRPN(self , tokens):
        self.expression = tokens.split()
        self.result = []
        for i in self.expression:
            if i not in '/*+-':
                self.result.append(int(i))
            else:
                R = self.result.pop()
                L = self.result.pop()
                if i == '+':
                    self.result.append(L+R)
                if i == '-':
                    self.result.append(L-R)
                if i == '*':
                    self.result.append(L*R)
                if i == '/':
                    self.result.append(int(L/R))
        return self.result.pop()


expression = "10 6 9 3 + -11 * / * 17 + 5 +"
a = Solution()
ans = a.evalRPN(expression)
# ans = evalRPN(self.expression)
print(ans)

        