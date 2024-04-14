
# Convert infix to postfix expression using stack 
a = {
    "+":1,
    "-":1,
    "*":2,
    "/":2
    }

def infix_to_postfix(expression):
    operator=[]
    operand=[]
    for i in expression:
        if i.isalnum():
            operand.append(i)
        
        elif i in a:
            while operator and a[i]<=a.get(operator[-1],0):
                operand.append(operator.pop())
            operator.append(i)

        elif i =='(':
            operator.append(i)
        
        elif i == ")":
            while operator and operator[-1] != "(":
                operand.append(operator.pop())
            operator.pop()
    while operator:
        operand.append(operator.pop())
    
    return operand

express = "(a+b)/(c-d)"
ans = infix_to_postfix(express)
print(''.join(ans))